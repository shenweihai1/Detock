#include "module/janus/scheduler.h"

#include <algorithm>
#include <unordered_map>
#include <unordered_set>

#include "common/json_utils.h"
#include "common/proto_utils.h"
#include "common/types.h"
#include "proto/internal.pb.h"

namespace janus {

using std::make_shared;
using std::move;
using std::shared_ptr;
using std::vector;
using std::chrono::milliseconds;

using slog::kMachineIdBits;
using slog::kPartitionIdBits;
using slog::kRegionIdBits;
using slog::kReplicaIdBits;
using slog::kSchedulerChannel;
using slog::MakeMachineId;
using slog::MakeRunnerFor;
using slog::internal::Request;
using slog::internal::Response;

PendingIndex::PendingIndex(int local_partition) : local_partition_(local_partition) {}

bool PendingIndex::Add(const JanusDependency& ancestor, TxnId descendant) {
  auto it = index_.find(ancestor.txn_id());
  if (it != index_.end()) {
    it->second.insert(descendant);
    return true;
  }
  // If current partition is not a participant of ancestor
  if ((ancestor.participants_bitmap() & (1 << local_partition_)) == 0) {
    index_[ancestor.txn_id()].insert(descendant);
    return true;
  }
  return false;
}

std::optional<std::unordered_set<TxnId>> PendingIndex::Remove(TxnId ancestor) {
  auto it = index_.find(ancestor);
  if (it == index_.end()) {
    return std::nullopt;
  }
  std::unordered_set<TxnId> descendants(std::move(it->second));
  index_.erase(it);
  return descendants;
}

Scheduler::Scheduler(const shared_ptr<Broker>& broker, const shared_ptr<Storage>& storage,
                     const MetricsRepositoryManagerPtr& metrics_manager, std::chrono::milliseconds poll_timeout)
    : NetworkedModule(broker, {kSchedulerChannel, false /* is_raw */}, metrics_manager, poll_timeout),
      sccs_finder_(graph_),
      pending_txns_(config()->local_partition()),
      current_worker_(0) {
  for (int i = 0; i < config()->num_workers(); i++) {
    workers_.push_back(MakeRunnerFor<Worker>(i, broker, storage, metrics_manager, poll_timeout));
  }
}

void Scheduler::Initialize() {
  auto cpus = config()->cpu_pinnings(slog::ModuleId::WORKER);
  size_t i = 0;
  for (auto& worker : workers_) {
    std::optional<uint32_t> cpu = {};
    if (i < cpus.size()) {
      cpu = cpus[i];
    }
    worker->StartInNewThread(cpu);

    zmq::socket_t worker_socket(*context(), ZMQ_PAIR);
    worker_socket.set(zmq::sockopt::rcvhwm, 0);
    worker_socket.set(zmq::sockopt::sndhwm, 0);
    worker_socket.bind(kSchedWorkerAddress + std::to_string(i));

    AddCustomSocket(move(worker_socket));

    i++;
  }
}

void Scheduler::OnInternalRequestReceived(EnvelopePtr&& env) {
  switch (env->request().type_case()) {
    case Request::kJanusCommit:
      ProcessTransaction(move(env));
      break;
    case Request::kJanusInquire:
      ProcessInquiry(move(env));
      break;
    default:
      LOG(ERROR) << "Unexpected request type received: \"" << CASE_NAME(env->request().type_case(), Request) << "\"";
      break;
  }
}

void Scheduler::OnInternalResponseReceived(EnvelopePtr&& env) {
  if (env->response().type_case() != Response::kJanusInquire) {
    LOG(ERROR) << "Unexpected response type received: \"" << CASE_NAME(env->response().type_case(), Response) << "\"";
  }
  auto& inquiry_result = env->response().janus_inquire();
  auto txn_id = inquiry_result.txn_id();
  if (inquiry_result.executed()) {
    execution_horizon_.Add(txn_id);
  } else {
    vector<JanusDependency> deps(inquiry_result.deps().begin(), inquiry_result.deps().end());
    graph_.insert({txn_id, Vertex{txn_id, std::move(deps)}});
  }
  CheckPendingTxns(txn_id);
}

// Handle responses from the workers
bool Scheduler::OnCustomSocket() {
  bool has_msg = false;
  bool stop = false;
  while (!stop) {
    stop = true;
    for (size_t i = 0; i < workers_.size(); i++) {
      if (zmq::message_t msg; GetCustomSocket(i).recv(msg, zmq::recv_flags::dontwait)) {
        stop = false;
        has_msg = true;
        auto txn_id = *msg.data<TxnId>();
        execution_horizon_.Add(txn_id);
        graph_.erase(txn_id);
      }
    }
  };

  return has_msg;
}

void Scheduler::ProcessTransaction(EnvelopePtr&& env) {
  auto commit = env->mutable_request()->mutable_janus_commit();
  auto txn = commit->release_txn();
  auto txn_id = txn->internal().id();

  txns_.emplace(txn_id, txn);

  vector<JanusDependency> deps(commit->deps().begin(), commit->deps().end());
  auto [vertex_it, inserted] = graph_.insert({txn_id, Vertex{txn_id, std::move(deps)}});
  CHECK(inserted);

  CheckPendingInquiry(txn_id);

  sccs_finder_.FindSCCs(vertex_it->second, execution_horizon_);
  auto result = sccs_finder_.Finalize();

  DispatchSCCs(result.sccs);
  InquireMissingDependencies(txn_id, result.missing_deps);
  CheckPendingTxns(txn_id);
}

void Scheduler::InquireMissingDependencies(TxnId txn_id, const vector<JanusDependency>& missing_deps) {
  auto local_region = config()->local_region();
  auto local_replica = config()->local_replica();
  auto env = NewEnvelope();
  for (const auto& dep : missing_deps) {
    if (pending_txns_.Add(dep, txn_id)) {
      auto inquiry = env->mutable_request()->mutable_janus_inquire();
      inquiry->set_txn_id(dep.txn_id());
      Send(*env, MakeMachineId(local_region, local_replica, dep.target_partition()), kSchedulerChannel);
    }
  }
}

bool Scheduler::ProcessInquiry(EnvelopePtr&& env) {
  auto txn_id = env->request().janus_inquire().txn_id();
  auto resp_env = NewEnvelope();
  auto resp_inquiry = resp_env->mutable_response()->mutable_janus_inquire();
  resp_inquiry->set_txn_id(txn_id);

  if (auto vertex_it = graph_.find(txn_id); vertex_it == graph_.end()) {
    if (execution_horizon_.contains(txn_id)) {
      resp_inquiry->set_executed(true);
    } else {
      pending_inquiries_.emplace(txn_id, move(env));
      return false;
    }
  } else {
    resp_inquiry->set_executed(false);
    for (auto& dep : vertex_it->second.deps) {
      resp_inquiry->add_deps()->CopyFrom(dep);
    }
  }

  Send(*resp_env, env->from(), kSchedulerChannel);
  return true;
}

void Scheduler::DispatchSCCs(const std::vector<SCC>& sccs) {
  for (const SCC& scc : sccs) {
    for (auto txn_id : scc) {
      auto txn_it = txns_.find(txn_id);
      CHECK(txn_it != txns_.end());

      zmq::message_t msg(sizeof(Transaction*));
      *msg.data<Transaction*>() = txn_it->second;
      txns_.erase(txn_it);

      int worker = current_worker_;
      current_worker_ = (current_worker_ + 1) % workers_.size();
      GetCustomSocket(worker).send(msg, zmq::send_flags::none);

      VLOG(3) << "Dispatched txn " << TXN_ID_STR(txn_id);
    }
  }
}

void Scheduler::CheckPendingInquiry(TxnId txn_id) {
  if (auto it = pending_inquiries_.find(txn_id); it != pending_inquiries_.end()) {
    CHECK(ProcessInquiry(move(it->second)));
    pending_inquiries_.erase(it);
  }
}

void Scheduler::CheckPendingTxns(TxnId txn_id) {
  std::unordered_set<TxnId> visited;

  auto pending = pending_txns_.Remove(txn_id);
  if (pending.has_value()) {
    for (auto pending_txn_id : pending.value()) {
      if (visited.find(pending_txn_id) == visited.end()) {
        auto pending_txn_it = graph_.find(pending_txn_id);
        CHECK(pending_txn_it != graph_.end());

        sccs_finder_.FindSCCs(pending_txn_it->second, execution_horizon_);
        auto result = sccs_finder_.Finalize();
        DispatchSCCs(result.sccs);
        InquireMissingDependencies(txn_id, result.missing_deps);
        visited.insert(result.visited.begin(), result.visited.end());
      }
    }
  }
}

}  // namespace janus
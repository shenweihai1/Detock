#include "module/sequencer.h"

#include "common/proto_utils.h"
#include "paxos/simple_multi_paxos.h"

namespace slog {

using internal::Batch;
using internal::Request;
using internal::Response;

Sequencer::Sequencer(
    shared_ptr<Configuration> config,
    Broker& broker)
  : BasicModule(
        broker.AddChannel(SEQUENCER_CHANNEL),
        config->GetBatchDuration() /* wake_up_every_ms */),
    config_(config),
    local_paxos_(new SimpleMultiPaxosClient(*this, LOCAL_PAXOS)),
    batch_(new Batch()),
    batch_id_counter_(0) {}

void Sequencer::HandleInternalRequest(
    Request&& req,
    string&& /* from_machine_id */) {
  switch (req.type_case()) {
    case Request::kForwardTxn: {
      // Received a single-home txn
      auto txn = req.mutable_forward_txn()->release_txn();
      PutSingleHomeTransactionIntoBatch(txn);
      break;
    }
    case Request::kForwardBatch: {
      // Received a batch of multi-home txns
      auto batch = req.mutable_forward_batch()->release_batch_data();
      ProcessMultiHomeBatch(batch);
      break;
    }
    default:
      LOG(ERROR) << "Unexpected request type received: \""
                 << CASE_NAME(req.type_case(), Request) << "\"";
      break;
  }
}

void Sequencer::HandlePeriodicWakeUp() {
  // Do nothing if there is nothing to send
  if (batch_->transactions().empty()) {
    return;
  }

  auto batch_id = NextBatchId();
  batch_->set_id(batch_id);

  VLOG(1) << "Finished batch " << batch_id
          << ". Sending out for ordering and replicating";

  Request req;
  auto forward_batch = req.mutable_forward_batch();
  // minus 1 so that it starts from 0
  forward_batch->set_same_origin_position(batch_id_counter_ - 1);
  forward_batch->set_allocated_batch_data(batch_.release());

  // Send batch id to local paxos for ordering
  local_paxos_->Propose(config_->GetLocalPartition());

  // Replicate batch to all machines
  for (uint32_t part = 0; part < config_->GetNumPartitions(); part++) {
    for (uint32_t rep = 0; rep < config_->GetNumReplicas(); rep++) {
      auto machine_id = MakeMachineIdAsString(rep, part);
      Send(req, machine_id, SCHEDULER_CHANNEL);
    }
  }

  batch_.reset(new Batch());
}

void Sequencer::ProcessMultiHomeBatch(internal::Batch* batch) {
  auto local_rep = config_->GetLocalReplica();
  while (!batch->transactions().empty()) {
    auto txn = batch->mutable_transactions()->ReleaseLast();
    auto& master_metadata = txn->internal().master_metadata();
    auto KeepLocalKeysOnly = [&master_metadata, local_rep](
        auto key_map) {
      auto it = key_map->begin();
      while (it != key_map->end()) {
        auto& metadata = master_metadata.at((*it).first);
        if (metadata.master() != local_rep) {
          it = key_map->erase(it);
        } else {
          it++;
        }
      }
    };

    KeepLocalKeysOnly(txn->mutable_read_set());
    KeepLocalKeysOnly(txn->mutable_write_set());

    txn->mutable_internal()->set_type(TransactionType::LOCK_ONLY);

    PutSingleHomeTransactionIntoBatch(txn);
  }
}

void Sequencer::PutSingleHomeTransactionIntoBatch(Transaction* txn) {
  CHECK(
      txn->internal().type() == TransactionType::SINGLE_HOME
      || txn->internal().type() == TransactionType::LOCK_ONLY)
      << "Sequencer batch can only contain single-home or lock-only txn. "
      << "Multi-home txn or unknown txn type received instead.";
  batch_->mutable_transactions()->AddAllocated(txn);
}

BatchId Sequencer::NextBatchId() {
  batch_id_counter_++;
  current_batch_id_ =
      batch_id_counter_ * MAX_NUM_MACHINES + config_->GetLocalMachineIdAsNumber();
  return current_batch_id_;
}

} // namespace slog
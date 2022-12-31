#pragma once

#include <unordered_map>

#include "common/configuration.h"
#include "common/metrics.h"
#include "common/sharder.h"
#include "common/types.h"
#include "connection/broker.h"
#include "module/base/networked_module.h"
#include "module/janus/phase.h"
#include "proto/transaction.pb.h"

namespace slog {

struct AcceptorTxnInfo {
  AcceptorTxnInfo(Transaction* txn) : 
      txn(txn), phase(Phase::PRE_ACCEPT), highest_ballot(0) {}

  Transaction* txn;
  Phase phase;
  int highest_ballot;
};

class JanusAcceptor : public NetworkedModule {
 public:
  JanusAcceptor(const std::shared_ptr<zmq::context_t>& context, const ConfigurationPtr& config,
                const MetricsRepositoryManagerPtr& metrics_manager,
                std::chrono::milliseconds poll_timeout_ms = kModuleTimeout);

  std::string name() const override { return "JanusAcceptor"; }

 protected:
  void OnInternalRequestReceived(EnvelopePtr&& env) final;

 private:
  void ProcessPreAccept(EnvelopePtr&& env);
  void ProcessAccept(EnvelopePtr&& env);
  void ProcessCommit(EnvelopePtr&& env);

  const SharderPtr sharder_;
  std::unordered_map<TxnId, AcceptorTxnInfo> txns_;
  std::unordered_map<Key, TxnId> latest_writing_txns_;
};

}  // namespace slog
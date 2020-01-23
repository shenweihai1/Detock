#include "module/scheduler_components/local_log.h"

#include <glog/logging.h>

namespace slog {

LocalLog::LocalLog() : next_slot_(0) {}

void LocalLog::AddBatch(BatchPtr batch) {
  unordered_batches_[batch->id()] = batch;
  UpdateReadyBatches();
}

void LocalLog::AddSlot(SlotId slot_id, BatchId batch_id) {
  if (pending_slots_.count(slot_id) > 0) {
    LOG(ERROR) << "Slot " << slot_id << " has already been taken.";
    return;
  }
  pending_slots_[slot_id] = batch_id;
  UpdateReadyBatches();
}

void LocalLog::AddSlottedBatch(SlotId slot_id, BatchPtr batch) {
  AddBatch(batch);
  AddSlot(slot_id, batch->id());
}

bool LocalLog::HasNextBatch() const {
  return !ready_batches_.empty();
}

BatchPtr LocalLog::NextBatch() {
  if (!HasNextBatch()) {
    throw std::runtime_error("NextBatch() was called when there is no batch");
  }
  auto next_batch = ready_batches_.front();
  ready_batches_.pop();
  return next_batch;
}

void LocalLog::UpdateReadyBatches() {
  while (pending_slots_.count(next_slot_) > 0) {
    auto next_batch_id = pending_slots_.at(next_slot_);
    if (unordered_batches_.count(next_batch_id) == 0) {
      break;
    }

    ready_batches_.emplace(unordered_batches_.at(next_batch_id));

    unordered_batches_.erase(next_batch_id);
    pending_slots_.erase(next_slot_);

    next_slot_++;
  }
}

} // namespace slog
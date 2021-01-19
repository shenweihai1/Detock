#include "module/base/module.h"

#include <glog/logging.h>

#include "common/constants.h"
#include "common/thread_utils.h"

using std::shared_ptr;
using std::unique_ptr;

namespace slog {

ModuleRunner::ModuleRunner(const shared_ptr<Module>& module) : module_(module), running_(false), setup_(false) {}

ModuleRunner::~ModuleRunner() {
  running_ = false;
  if (thread_.joinable()) {
    thread_.join();
  }
}

void ModuleRunner::Start(std::optional<uint32_t> cpu) {
  if (running_) {
    throw std::runtime_error("The module has already started");
  }
  running_ = true;
  if (cpu.has_value()) {
    PinToCpu(pthread_self(), cpu.value());
  }
  Run();
}

void ModuleRunner::StartInNewThread(std::optional<uint32_t> cpu) {
  if (running_) {
    throw std::runtime_error("The module has already started");
  }
  running_ = true;
  thread_ = std::thread(&ModuleRunner::Run, this);
  if (cpu.has_value()) {
    PinToCpu(thread_.native_handle(), cpu.value());
  }
}

void ModuleRunner::StartOnce() {
  if (running_) {
    throw std::runtime_error("The module has already started");
  }
  SetUpOnce();
  module_->Loop();
}

void ModuleRunner::Run() {
  SetUpOnce();
  while (running_) {
    if (module_->Loop()) Stop();
  }
}

void ModuleRunner::SetUpOnce() {
  if (!setup_) {
    module_->SetUp();
    setup_ = true;
  }
}

void ModuleRunner::Stop() { running_ = false; }

}  // namespace slog
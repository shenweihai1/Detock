#pragma once

#include <queue>

namespace slog {

template <typename T>
class RollingWindow {
 public:
  RollingWindow(size_t sz) : size_(sz), sum_(0) {}

  void Add(T val) {
    buffer_.push(val);
    sum_ += val;
    if (buffer_.size() > size_) {
      sum_ -= buffer_.front();
      buffer_.pop();
    }
  }

  T sum() const { return sum_; }
  float avg() const { return static_cast<float>(sum_) / buffer_.size(); }

 private:
  size_t size_;
  std::queue<T> buffer_;
  T sum_;
};

}  // namespace slog
# utils/performance_monitor.py

import time

class PerformanceMonitor:
    """Class for monitoring performance metrics."""
    
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        """Starts the performance monitoring."""
        self.start_time = time.time()

    def stop(self):
        """Stops the performance monitoring and returns the elapsed time."""
        self.end_time = time.time()
        return self.elapsed_time()

    def elapsed_time(self):
        """Calculates the elapsed time in seconds."""
        if self.start_time is None or self.end_time is None:
            raise RuntimeError("Performance monitoring has not been started or stopped.")
        return self.end_time - self.start_time

# Example usage
if __name__ == "__main__":
    monitor = PerformanceMonitor()
    monitor.start()
    time.sleep(1)  # Simulate a process
    elapsed = monitor.stop()
    print(f"Elapsed time: {elapsed:.2f} seconds")

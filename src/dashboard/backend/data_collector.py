# src/dashboard/backend/data_collector.py

import random
import time
import requests
import logging
import os
import signal
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MetricCollector:
    def __init__(self, metric_name="network_latency", value_range=(10, 100), interval=5):
        self.metric_name = metric_name
        self.value_range = value_range
        self.interval = interval
        self.running = True

    def collect_metric(self):
        """Simulate collecting a single metric."""
        value = random.uniform(*self.value_range)
        return {"name": self.metric_name, "value": value}

    def send_metric(self, metric):
        """Send the collected metric to the API."""
        try:
            response = requests.post("http://localhost:8000/api/v1/metrics/", json=metric)
            response.raise_for_status()  # Raise an error for bad responses
            logging.info(f"Collected Metric: {metric}, Response: {response.status_code}")
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to send metric: {e}")

    def run(self):
        """Run the metric collection loop."""
        while self.running:
            metric = self.collect_metric()
            self.send_metric(metric)
            time.sleep(self.interval)

    def stop(self):
        """Stop the metric collection gracefully."""
        self.running = False
        logging.info("Stopping metric collection.")

def signal_handler(sig, frame):
    """Handle termination signals."""
    collector.stop()
    sys.exit(0)

if __name__ == "__main__":
    # Load configuration from environment variables or use defaults
    metric_name = os.getenv("METRIC_NAME", "network_latency")
    value_range = (float(os.getenv("VALUE_MIN", 10)), float(os.getenv("VALUE_MAX", 100)))
    interval = int(os.getenv("COLLECTION_INTERVAL", 5))

    collector = MetricCollector(metric_name, value_range, interval)

    # Register signal handlers for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    logging.info("Starting metric collection...")
    collector.run()

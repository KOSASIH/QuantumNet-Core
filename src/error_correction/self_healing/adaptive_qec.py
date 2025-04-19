import logging
import numpy as np
import matplotlib.pyplot as plt

class AdaptiveQEC:
    def __init__(self, initial_error_threshold, strategies):
        """
        Initialize the Adaptive QEC system.

        :param initial_error_threshold: Initial threshold for error adaptation.
        :param strategies: A dictionary of QEC strategies to choose from.
        """
        self.error_threshold = initial_error_threshold
        self.strategies = strategies  # Dictionary of strategies
        self.current_strategy = None
        self.history = []  # To track error rates and strategies used

        # Set up logging
        logging.basicConfig(level=logging.INFO)

    def adapt(self, error_rate):
        """Adapt the QEC strategy based on the current error rate."""
        logging.info(f"Current error rate: {error_rate:.2f}")

        if error_rate > self.error_threshold:
            logging.info("Error rate exceeds threshold. Adapting QEC strategy.")
            self.current_strategy = self.select_strategy(error_rate)
            self.history.append((error_rate, self.current_strategy))
            logging.info(f"Switched to strategy: {self.current_strategy}")
        else:
            logging.info("Error rate is within acceptable limits. No adaptation needed.")

    def select_strategy(self, error_rate):
        """Select the appropriate QEC strategy based on the error rate."""
        if error_rate < 0.01:
            return self.strategies['low_error']
        elif error_rate < 0.05:
            return self.strategies['medium_error']
        else:
            return self.strategies['high_error']

    def adjust_threshold(self, historical_data):
        """Dynamically adjust the error threshold based on historical data."""
        if historical_data:
            self.error_threshold = np.mean(historical_data) + np.std(historical_data)
            logging.info(f"Adjusted error threshold to: {self.error_threshold:.2f}")

    def simulate_error_rates(self, num_samples=100):
        """Simulate error rates for testing the adaptive QEC."""
        simulated_rates = np.random.rand(num_samples)  # Simulate random error rates
        for rate in simulated_rates:
            self.adapt(rate)

    def visualize_performance(self):
        """Visualize the performance of different QEC strategies over time."""
        if not self.history:
            logging.warning("No adaptation history to visualize.")
            return

        error_rates, strategies = zip(*self.history)
        plt.figure(figsize=(10, 6))
        plt.plot(error_rates, label='Error Rate', marker='o')
        plt.axhline(y=self.error_threshold, color='r', linestyle='--', label='Threshold')
        plt.title("Adaptive QEC Performance")
        plt.xlabel("Adaptation Steps")
        plt.ylabel("Error Rate")
        plt.xticks(range(len(error_rates)))
        plt.yticks(np.arange(0, 1.1, 0.1))
        plt.legend()
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    strategies = {
        'low_error': 'Surface Code',
        'medium_error': 'Concatenated Code',
        'high_error': 'Shor Code'
    }
    adaptive_qec = AdaptiveQEC(initial_error_threshold=0.05, strategies=strategies)
    adaptive_qec.simulate_error_rates(num_samples=50)
    adaptive_qec.visualize_performance()

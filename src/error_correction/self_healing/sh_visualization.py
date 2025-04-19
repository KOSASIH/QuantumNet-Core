import matplotlib.pyplot as plt
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def visualize_error_correction_process(error_rates, correction_success_rates=None, time_steps=None):
    """Visualize the error correction process.

    :param error_rates: List of error rates over time.
    :param correction_success_rates: Optional list of correction success rates over time.
    :param time_steps: Optional list of time steps corresponding to the data.
    """
    if time_steps is None:
        time_steps = np.arange(len(error_rates))

    plt.figure(figsize=(12, 6))
    
    # Plot error rates
    plt.plot(time_steps, error_rates, label='Error Rate', color='red', marker='o', linestyle='-', alpha=0.7)
    
    # Plot correction success rates if provided
    if correction_success_rates is not None:
        plt.plot(time_steps, correction_success_rates, label='Correction Success Rate', color='green', marker='x', linestyle='--', alpha=0.7)

    plt.title("Error Correction Process")
    plt.xlabel("Time Steps")
    plt.ylabel("Rate")
    plt.axhline(y=np.mean(error_rates), color='blue', linestyle='--', label='Mean Error Rate')
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()
    logging.info("Displayed error correction process visualization.")

def visualize_error_distribution(errors):
    """Visualize the distribution of errors.

    :param errors: List of error values.
    """
    plt.figure(figsize=(10, 6))
    plt.hist(errors, bins=20, alpha=0.7, color='blue', edgecolor='black')
    plt.title("Error Distribution")
    plt.xlabel("Error Value")
    plt.ylabel("Frequency")
    plt.grid(axis='y', alpha=0.75)
    plt.tight_layout()
    plt.show()
    logging.info("Displayed error distribution visualization.")

def save_visualization(filename):
    """Save the current figure to a file.

    :param filename: The filename to save the figure as.
    """
    plt.savefig(filename)
    logging.info(f"Saved visualization to {filename}.")

# Example usage
if __name__ == "__main__":
    # Simulated data for demonstration
    error_rates = np.random.rand(100) * 0.1  # Simulated error rates
    correction_success_rates = np.random.rand(100) * 0.9  # Simulated success rates

    visualize_error_correction_process(error_rates, correction_success_rates)
    visualize_error_distribution(np.random.randint(0, 10, size=100))  # Simulated error values

import numpy as np
import logging
import matplotlib.pyplot as plt

# Set up logging
logging.basicConfig(level=logging.INFO)

def calculate_error_rate(errors):
    """Calculate the error rate from a list of errors."""
    if not errors:
        logging.warning("No errors provided. Returning error rate of 0.")
        return 0.0
    error_rate = sum(errors) / len(errors)
    logging.info(f"Calculated error rate: {error_rate:.2f}")
    return error_rate

def classify_errors(errors, thresholds):
    """Classify errors based on severity thresholds.

    :param errors: List of error values.
    :param thresholds: Dictionary with severity levels and their corresponding thresholds.
    :return: Dictionary with counts of classified errors.
    """
    classified = {key: 0 for key in thresholds.keys()}
    for error in errors:
        for severity, threshold in thresholds.items():
            if error >= threshold:
                classified[severity] += 1
                break
    logging.info(f"Classified errors: {classified}")
    return classified

def simulate_errors(num_errors, error_probability, size):
    """Simulate a list of errors based on a given probability.

    :param num_errors: Number of errors to simulate.
    :param error_probability: Probability of an error occurring.
    :param size: Size of the quantum system (number of qubits).
    :return: List of simulated errors.
    """
    errors = np.random.binomial(1, error_probability, (num_errors, size))
    logging.info(f"Simulated {num_errors} errors with probability {error_probability}.")
    return errors.tolist()

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
    plt.show()
    logging.info("Displayed error distribution.")

def visualize_error_rates(error_rates):
    """Visualize error rates over time.

    :param error_rates: List of error rates.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(error_rates, marker='o', linestyle='-', color='red')
    plt.title("Error Rates Over Time")
    plt.xlabel("Time Step")
    plt.ylabel("Error Rate")
    plt.axhline(y=np.mean(error_rates), color='blue', linestyle='--', label='Mean Error Rate')
    plt.legend()
    plt.grid()
    plt.show()
    logging.info("Displayed error rates over time.")

# Example usage
if __name__ == "__main__":
    # Simulate some errors
    simulated_errors = simulate_errors(num_errors=1000, error_probability=0.1, size=5)
    error_rates = [calculate_error_rate(errors) for errors in simulated_errors]
    
    # Classify errors
    thresholds = {'low': 0.1, 'medium': 0.5, 'high': 1.0}
    classified_errors = classify_errors([sum(errors) for errors in simulated_errors], thresholds)
    
    # Visualize results
    visualize_error_distribution([sum(errors) for errors in simulated_errors])
    visualize_error_rates(error_rates)

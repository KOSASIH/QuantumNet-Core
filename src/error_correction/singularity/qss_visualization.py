"""
Visualization utilities for the Quantum Singularity Shield (QSS).
This module provides functions for visualizing quantum states, probability distributions,
and results from anomaly detection.
"""

import numpy as np
import matplotlib.pyplot as plt

def visualize_quantum_state(state: np.ndarray, title: str = "Quantum State Visualization"):
    """
    Visualize the quantum state using a bar chart.

    Args:
        state (np.ndarray): The quantum state to visualize.
        title (str): The title of the plot.
    """
    plt.figure(figsize=(10, 5))
    plt.bar(range(len(state)), np.abs(state)**2, color='blue', alpha=0.7)
    plt.title(title)
    plt.xlabel("Basis States")
    plt.ylabel("Probability Amplitude")
    plt.xticks(range(len(state)), [f"|{i}> " for i in range(len(state))])
    plt.grid()
    plt.show()

def visualize_probability_distribution(probabilities: np.ndarray, title: str = "Probability Distribution"):
    """
    Visualize the probability distribution of a quantum state.

    Args:
        probabilities (np.ndarray): The probability distribution to visualize.
        title (str): The title of the plot.
    """
    plt.figure(figsize=(10, 5))
    plt.bar(range(len(probabilities)), probabilities, color='green', alpha=0.7)
    plt.title(title)
    plt.xlabel("Basis States")
    plt.ylabel("Probability")
    plt.xticks(range(len(probabilities)), [f"|{i}> " for i in range(len(probabilities))])
    plt.ylim(0, 1)
    plt.grid()
    plt.show()

def visualize_anomaly_detection_results(results: list, title: str = "Anomaly Detection Results"):
    """
    Visualize the results of anomaly detection.

    Args:
        results (list): A list of boolean values indicating anomalies.
        title (str): The title of the plot.
    """
    plt.figure(figsize=(10, 5))
    plt.plot(results, marker='o', linestyle='-', color='blue')
    plt.title(title)
    plt.xlabel("Sample Index")
    plt.ylabel("Anomaly Detected (1 = Yes, 0 = No)")
    plt.yticks([0, 1], ['No', 'Yes'])
    plt.grid()
    plt.show()

def visualize_singularity_effects(original_states: list, modified_states: list):
    """
    Visualize the effects of singularities on quantum states.

    Args:
        original_states (list): A list of original quantum states.
        modified_states (list): A list of modified quantum states after singularity effects.
    """
    num_samples = len(original_states)
    fig, axes = plt.subplots(num_samples, 2, figsize=(10, 5 * num_samples))

    for i in range(num_samples):
        axes[i, 0].bar(range(len(original_states[i])), np.abs(original_states[i])**2, color='blue', alpha=0.7)
        axes[i, 0].set_title(f"Original State {i+1}")
        axes[i, 0].set_xlabel("Basis States")
        axes[i, 0].set_ylabel("Probability Amplitude")

        axes[i, 1].bar(range(len(modified_states[i])), np.abs(modified_states[i])**2, color='red', alpha=0.7)
        axes[i, 1].set_title(f"Modified State {i+1} (After Singularity Effect)")
        axes[i, 1].set_xlabel("Basis States")
        axes[i, 1].set_ylabel("Probability Amplitude")

    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    # Example quantum state
    state = np.array([1/np.sqrt(2), 1/np.sqrt(2), 0, 0])  # |0> + |1>
    visualize_quantum_state(state)

    # Example probability distribution
    probabilities = np.abs(state)**2
    visualize_probability_distribution(probabilities)

    # Example anomaly detection results
    anomaly_results = [0, 1, 0, 0, 1, 0, 0, 1]
    visualize_anomaly_detection_results(anomaly_results)

    # Example singularity effects visualization
    original_states = [state, state]
    modified_states = [state * 0.8, state * 1.2]  # Simulated effects
    visualize_singularity_effects(original_states, modified_states)

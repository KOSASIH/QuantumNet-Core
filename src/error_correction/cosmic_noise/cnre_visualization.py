"""
Visualization Tools for Analyzing Noise and Mitigation Strategies in CNRE
"""
import numpy as np
import matplotlib.pyplot as plt
from qiskit.visualization import plot_histogram, plot_state_qsphere
from qiskit.quantum_info import Statevector

def plot_noise_histogram(noisy_states, title='Noise Distribution', xlabel='State', ylabel='Frequency'):
    """
    Plot a histogram of the distribution of noisy states.

    Parameters:
    noisy_states (list of Statevector): List of noisy quantum states.
    title (str): Title of the histogram.
    xlabel (str): Label for the x-axis.
    ylabel (str): Label for the y-axis.
    """
    # Convert states to measurement outcomes
    outcomes = [state.measure() for state in noisy_states]
    counts = {outcome: outcomes.count(outcome) for outcome in set(outcomes)}
    
    plot_histogram(counts)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def visualize_state(state: Statevector, title='Quantum State'):
    """
    Visualize a quantum state using a Q-sphere.

    Parameters:
    state (Statevector): The quantum state to visualize.
    title (str): Title for the visualization.
    """
    plot_state_qsphere(state)
    plt.title(title)
    plt.show()

def compare_states(original_state: Statevector, noisy_state: Statevector, title='State Comparison'):
    """
    Compare the original and noisy quantum states using Q-sphere visualization.

    Parameters:
    original_state (Statevector): The original quantum state.
    noisy_state (Statevector): The noisy quantum state.
    title (str): Title for the comparison.
    """
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    
    # Original state
    ax[0].set_title('Original State')
    plot_state_qsphere(original_state, ax=ax[0])
    
    # Noisy state
    ax[1].set_title('Noisy State')
    plot_state_qsphere(noisy_state, ax=ax[1])
    
    plt.suptitle(title)
    plt.show()

def plot_fidelity_over_epochs(fidelity_values, title='Fidelity Over Epochs'):
    """
    Plot the fidelity of states over training epochs.

    Parameters:
    fidelity_values (list of float): List of fidelity values over epochs.
    title (str): Title for the plot.
    """
    plt.plot(fidelity_values, marker='o')
    plt.title(title)
    plt.xlabel('Epochs')
    plt.ylabel('Fidelity')
    plt.grid()
    plt.show()

def plot_error_rates(error_rates, title='Error Rates Over Time'):
    """
    Plot the error rates over time or epochs.

    Parameters:
    error_rates (list of float): List of error rates.
    title (str): Title for the plot.
    """
    plt.plot(error_rates, marker='x', color='red')
    plt.title(title)
    plt.xlabel('Time / Epochs')
    plt.ylabel('Error Rate')
    plt.grid()
    plt.show()

# Example usage:
# original_state = Statevector.from_dict({'00': 1, '01': 0, '10': 0, '11': 0})
# noisy_state = apply_noise(original_state, noise_type='depolarizing', noise_level=0.1)
# compare_states(original_state, noisy_state)
# plot_fidelity_over_epochs([0.9, 0.85, 0.88, 0.92])
# plot_error_rates([0.1, 0.15, 0.12, 0.08])

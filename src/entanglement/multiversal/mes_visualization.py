"""
Multiversal Entanglement Synchronizer Visualization Utilities.
This module provides functions for visualizing quantum states,
entanglement, and measurement results in a multiversal context.
"""

import numpy as np
import matplotlib.pyplot as plt
from qiskit.visualization import plot_bloch_multivector, plot_histogram

def visualize_state_on_bloch_sphere(state_vector: np.ndarray):
    """
    Visualize a quantum state on the Bloch sphere.

    Args:
        state_vector (np.ndarray): The quantum state vector to visualize.
    """
    # Ensure the state vector is normalized
    state_vector = state_vector / np.linalg.norm(state_vector)
    
    # Plot the state on the Bloch sphere
    plot_bloch_multivector(state_vector)
    plt.title("Quantum State on Bloch Sphere")
    plt.show()

def visualize_density_matrix(density_matrix: np.ndarray):
    """
    Visualize the density matrix of a quantum state.

    Args:
        density_matrix (np.ndarray): The density matrix to visualize.
    """
    plt.imshow(np.real(density_matrix), cmap='viridis', interpolation='nearest')
    plt.colorbar()
    plt.title("Density Matrix")
    plt.xlabel("Basis States")
    plt.ylabel("Basis States")
    plt.show()

def visualize_measurement_results(counts: dict):
    """
    Visualize the measurement results as a histogram.

    Args:
        counts (dict): The measurement results to visualize.
    """
    plot_histogram(counts)
    plt.title("Measurement Results")
    plt.xlabel("States")
    plt.ylabel("Counts")
    plt.show()

def visualize_entanglement_entropy(entropy_values: list):
    """
    Visualize the entanglement entropy over multiple states.

    Args:
        entropy_values (list): A list of entanglement entropy values to visualize.
    """
    plt.plot(entropy_values, marker='o')
    plt.title("Entanglement Entropy Over States")
    plt.xlabel("State Index")
    plt.ylabel("Entanglement Entropy")
    plt.grid()
    plt.show()

def visualize_entangled_states(state1: np.ndarray, state2: np.ndarray):
    """
    Visualize two entangled quantum states on the Bloch sphere.

    Args:
        state1 (np.ndarray): The first quantum state vector.
        state2 (np.ndarray): The second quantum state vector.
    """
    fig, ax = plt.subplots(1, 2, subplot_kw={'projection': '3d'}, figsize=(12, 6))
    
    # Normalize states
    state1 = state1 / np.linalg.norm(state1)
    state2 = state2 / np.linalg.norm(state2)

    # Plot state 1
    plot_bloch_multivector(state1, ax=ax[0])
    ax[0].set_title("State 1 on Bloch Sphere")

    # Plot state 2
    plot_bloch_multivector(state2, ax=ax[1])
    ax[1].set_title("State 2 on Bloch Sphere")

    plt.show()

# Example usage
if __name__ == "__main__":
    # Example quantum state vector
    state_vector = np.array([1/np.sqrt(2), 0, 1/np.sqrt(2), 0])  # Example state |00> + |11>
    
    # Visualize the state on the Bloch sphere
    visualize_state_on_bloch_sphere(state_vector)

    # Example density matrix
    density_matrix = np.outer(state_vector, state_vector.conj())
    
    # Visualize the density matrix
    visualize_density_matrix(density_matrix)

    # Example measurement results
    measurement_counts = {'00': 500, '01': 300, '10': 150, '11': 50}
    
    # Visualize measurement results
    visualize_measurement_results(measurement_counts)

    # Example entanglement entropy values
    entropy_values = [0.5, 0.7, 0.9, 0.6, 0.8]
    
    # Visualize entanglement entropy
    visualize_entanglement_entropy(entropy_values)

    # Example entangled states
    state1 = np.array([1/np.sqrt(2), 0, 1/np.sqrt(2), 0])  # |00> + |11>
    state2 = np.array([0, 1/np.sqrt(2), 0, 1/np.sqrt(2)])  # |01> + |10>
    
    # Visualize two entangled states
    visualize_entangled_states(state1, state2)

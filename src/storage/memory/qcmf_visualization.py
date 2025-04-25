"""
Visualization Utilities for Quantum Cosmic Memory Fabric (QCMF).
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from qiskit.visualization import plot_bloch_multivector, plot_histogram

def plot_quantum_state(state: np.ndarray, title: str = "Quantum State Visualization"):
    """
    Visualize a quantum state on the Bloch sphere.

    Args:
        state (np.ndarray): Quantum state to visualize.
        title (str): Title of the plot.
    """
    if state.shape[0] != 2**1:
        raise ValueError("State must be a single qubit state for Bloch sphere visualization.")
    
    plot_bloch_multivector(state)
    plt.title(title)
    plt.show()

def plot_memory_distribution(memory: list, title: str = "Memory Distribution"):
    """
    Visualize the distribution of memory states.

    Args:
        memory (list): List of memory states to visualize.
        title (str): Title of the plot.
    """
    plt.figure(figsize=(10, 6))
    plt.hist(memory, bins=20, alpha=0.7, color='blue', edgecolor='black')
    plt.title(title)
    plt.xlabel("Memory State Value")
    plt.ylabel("Frequency")
    plt.grid()
    plt.show()

def plot_state_vector(state: np.ndarray, title: str = "State Vector Visualization"):
    """
    Visualize the state vector of a quantum state.

    Args:
        state (np.ndarray): Quantum state vector to visualize.
        title (str): Title of the plot.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(state)), np.abs(state)**2, color='purple', alpha=0.7)
    plt.title(title)
    plt.xlabel("Basis States")
    plt.ylabel("Probability Amplitude")
    plt.xticks(range(len(state)), [f"|{i}>" for i in range(len(state))])
    plt.grid()
    plt.show()

def plot_memory_structure(memory_matrix: np.ndarray, title: str = "Memory Structure Visualization"):
    """
    Visualize the memory structure as a heatmap.

    Args:
        memory_matrix (np.ndarray): Memory matrix to visualize.
        title (str): Title of the plot.
    """
    plt.figure(figsize=(8, 6))
    plt.imshow(memory_matrix, cmap='viridis', interpolation='nearest')
    plt.colorbar(label='Memory Value')
    plt.title(title)
    plt.xlabel("Memory Address")
    plt.ylabel("Memory Address")
    plt.show()

def plot_3d_memory(memory: np.ndarray, title: str = "3D Memory Visualization"):
    """
    Visualize memory states in 3D.

    Args:
        memory (np.ndarray): Memory states to visualize.
        title (str): Title of the plot.
    """
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    x = np.arange(memory.shape[0])
    y = np.arange(memory.shape[1])
    x, y = np.meshgrid(x, y)
    ax.scatter(x, y, memory.flatten(), c=memory.flatten(), cmap='viridis')
    ax.set_title(title)
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")
    ax.set_zlabel("Memory Value")
    plt.show()

# Example usage
if __name__ == "__main__":
    # Example quantum state for visualization
    example_state = np.array([1/np.sqrt(2), 1/np.sqrt(2)])  # |+> state
    plot_quantum_state(example_state)

    # Example memory distribution
    example_memory = np.random.rand(1000)  # Random memory states
    plot_memory_distribution(example_memory)

    # Example state vector visualization
    example_state_vector = np.array([0.5, 0.5, 0.5, 0.5])  # Example state vector
    plot_state_vector(example_state_vector)

    # Example memory structure visualization
    example_memory_matrix = np.random.rand(10, 10)  # Random memory matrix
    plot_memory_structure(example_memory_matrix)

    # Example 3D memory visualization
    example_3d_memory = np.random.rand(10, 10)  # Random 3D memory states
    plot_3d_memory(example_3d_memory)

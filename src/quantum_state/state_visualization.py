# quantum_state/state_visualization.py

import matplotlib.pyplot as plt
import numpy as np
from .state_vector import StateVector
from .density_matrix import DensityMatrix

def visualize_state(state):
    """Visualizes the quantum state represented by a state vector or density matrix.
    
    Args:
        state (StateVector or DensityMatrix): The quantum state to visualize.
    
    Raises:
        ValueError: If the state type is unsupported.
    """
    if isinstance(state, StateVector):
        visualize_state_vector(state)
    elif isinstance(state, DensityMatrix):
        visualize_density_matrix(state)
    else:
        raise ValueError("Unsupported state type for visualization.")

def visualize_state_vector(state):
    """Visualizes the probability distribution of a quantum state vector.
    
    Args:
        state (StateVector): The quantum state vector to visualize.
    """
    plt.figure(figsize=(8, 4))
    probabilities = np.abs(state.amplitudes) ** 2
    plt.bar(range(len(state.amplitudes)), probabilities, color='blue', alpha=0.7)
    plt.title('State Vector Probability Distribution')
    plt.xlabel('Basis States')
    plt.ylabel('Probability Amplitude')
    plt.xticks(range(len(state.amplitudes)), [f'|{i}⟩' for i in range(len(state.amplitudes))])
    plt.ylim(0, 1)  # Set y-axis limits to [0, 1]
    plt.grid(axis='y')
    plt.show()

def visualize_density_matrix(state):
    """Visualizes the magnitude of a density matrix.
    
    Args:
        state (DensityMatrix): The density matrix to visualize.
    """
    plt.figure(figsize=(6, 6))
    plt.imshow(np.abs(state.matrix), cmap='viridis', interpolation='nearest')
    plt.title('Density Matrix Magnitude')
    plt.colorbar(label='Magnitude')
    plt.xlabel('Basis States')
    plt.ylabel('Basis States')
    plt.xticks(range(state.matrix.shape[0]), [f'|{i}⟩' for i in range(state.matrix.shape[0])])
    plt.yticks(range(state.matrix.shape[0]), [f'|{i}⟩' for i in range(state.matrix.shape[0])])
    plt.grid(False)  # Disable grid for density matrix visualization
    plt.show()

# Example usage
if __name__ == "__main__":
    from .state_vector import StateVector
    from .density_matrix import DensityMatrix

    state_vector = StateVector([1, 0, 0, 0])  # |0⟩ state
    density_matrix = DensityMatrix([[1, 0], [0, 0]])  # |0⟩ state
    visualize_state(state_vector)
    visualize_state(density_matrix)

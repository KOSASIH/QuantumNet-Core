# entanglement/entangler.py

import numpy as np
from scipy.linalg import sqrtm

class QuantumState:
    """Class representing a quantum state."""
    
    def __init__(self, amplitudes):
        self.amplitudes = np.array(amplitudes, dtype=complex)
        self.normalize()

    def normalize(self):
        """Normalizes the quantum state vector."""
        norm = np.linalg.norm(self.amplitudes)
        if norm == 0:
            raise ValueError("Cannot normalize a zero vector.")
        self.amplitudes /= norm

    def __repr__(self):
        return f"QuantumState(amplitudes={self.amplitudes})"

def create_entangled_pair():
    """Creates a pair of entangled qubits in a Bell state."""
    # Example: Creating a Bell state |Φ+⟩ = (|00⟩ + |11⟩) / √2
    state_0 = QuantumState([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)])  # |Φ+⟩ state
    state_1 = QuantumState([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)])  # Entangled with state_0
    return state_0, state_1

def measure_entanglement(qubit1, qubit2):
    """Measures the degree of entanglement between two qubits using the Concurrence measure."""
    # Calculate the density matrix for the combined state
    density_matrix = np.outer(qubit1.amplitudes, np.conjugate(qubit1.amplitudes)) + \
                     np.outer(qubit2.amplitudes, np.conjugate(qubit2.amplitudes))
    
    # Calculate the eigenvalues of the density matrix
    eigenvalues = np.linalg.eigvals(density_matrix)
    eigenvalues = np.sort(np.real(eigenvalues))  # Sort eigenvalues

    # Calculate the concurrence
    concurrence = max(0, eigenvalues[-1] - sum(eigenvalues[:-1]))
    return concurrence

def visualize_entangled_pair(qubit1, qubit2):
    """Visualizes the entangled state of two qubits."""
    import matplotlib.pyplot as plt

    # Prepare data for visualization
    states = [qubit1.amplitudes, qubit2.amplitudes]
    labels = ['Qubit 1', 'Qubit 2']
    
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    
    for i, state in enumerate(states):
        ax[i].bar(range(len(state)), np.abs(state)**2, color='b', alpha=0.6, label='Probability Amplitude')
        ax[i].set_title(f'{labels[i]} State')
        ax[i].set_xlabel('Basis States')
        ax[i].set_ylabel('Probability')
        ax[i].set_xticks(range(len(state)))
        ax[i].set_xticklabels([f'|{j}⟩' for j in range(len(state))])
        ax[i].legend()

    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    qubit1, qubit2 = create_entangled_pair()
    print(f"Created Entangled Pair:\n{qubit1}\n{qubit2}")
    
    entanglement_degree = measure_entanglement(qubit1, qubit2)
    print(f"Degree of Entanglement: {entanglement_degree}")

    visualize_entangled_pair(qubit1, qubit2)

# entanglement/entanglement_visualization.py

import matplotlib.pyplot as plt
import numpy as np

def visualize_entanglement(qubit1, qubit2):
    """Visualizes the entangled state of two qubits.
    
    Args:
        qubit1 (QuantumState): The first quantum state.
        qubit2 (QuantumState): The second quantum state.
    """
    # Prepare data for visualization
    states = [qubit1.amplitudes, qubit2.amplitudes]
    labels = ['Qubit 1', 'Qubit 2']
    
    # Create subplots for real and imaginary parts
    fig, ax = plt.subplots(2, 2, figsize=(12, 10))

    # Plotting the real parts
    for i, state in enumerate(states):
        ax[0, i].bar(range(len(state)), np.real(state), color='b', alpha=0.6, label='Real Part')
        ax[0, i].set_title(f'{labels[i]} - Real Part')
        ax[0, i].set_xlabel('Basis States')
        ax[0, i].set_ylabel('Amplitude')
        ax[0, i].set_xticks(range(len(state)))
        ax[0, i].set_xticklabels([f'|{j}⟩' for j in range(len(state))])
        ax[0, i].legend()

    # Plotting the imaginary parts
    for i, state in enumerate(states):
        ax[1, i].bar(range(len(state)), np.imag(state), color='r', alpha=0.6, label='Imaginary Part')
        ax[1, i].set_title(f'{labels[i]} - Imaginary Part')
        ax[1, i].set_xlabel('Basis States')
        ax[1, i].set_ylabel('Amplitude')
        ax[1, i].set_xticks(range(len(state)))
        ax[1, i].set_xticklabels([f'|{j}⟩' for j in range(len(state))])
        ax[1, i].legend()

    plt.tight_layout()
    plt.show()

def visualize_entangled_pair(qubit1, qubit2):
    """Visualizes the entangled state of two qubits in a combined plot.
    
    Args:
        qubit1 (QuantumState): The first quantum state.
        qubit2 (QuantumState): The second quantum state.
    """
    # Calculate the combined state for visualization
    combined_state = np.kron(qubit1.amplitudes, qubit2.amplitudes)
    
    # Prepare data for visualization
    x = np.arange(len(combined_state))
    
    # Create a bar plot for the combined state
    plt.figure(figsize=(12, 6))
    plt.bar(x, np.abs(combined_state)**2, color='purple', alpha=0.7)
    plt.title('Combined State Probability Distribution')
    plt.xlabel('Combined Basis States')
    plt.ylabel('Probability Amplitude')
    plt.xticks(x, [f'|{i}⟩' for i in range(len(combined_state))])
    plt.grid(axis='y')
    plt.show()

# Example usage
if __name__ == "__main__":
    from entangler import create_entangled_pair
    qubit1, qubit2 = create_entangled_pair()
    visualize_entanglement(qubit1, qubit2)
    visualize_entangled_pair(qubit1, qubit2)

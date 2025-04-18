# quantum_circuit/circuit_visualization.py

import matplotlib.pyplot as plt
import numpy as np
from .circuit import QuantumCircuit

def visualize_circuit(circuit):
    """Visualizes the quantum circuit.
    
    Args:
        circuit (QuantumCircuit): The quantum circuit to visualize.
    
    Raises:
        ValueError: If the circuit is empty or invalid.
    """
    if not circuit.get_circuit():
        raise ValueError("The circuit is empty. No gates to visualize.")
    
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.set_title('Quantum Circuit')
    ax.set_xlabel('Qubits')
    ax.set_ylabel('Operations')

    # Draw the gates in the circuit
    for i, (gate, qubits) in enumerate(circuit.get_circuit()):
        for qubit in qubits:
            ax.text(qubit, -i, '●', fontsize=20, ha='center', va='center', color='blue')
            ax.text(qubit, -i - 0.1, f'Gate {i + 1}', fontsize=10, ha='center', va='center', color='black')

    ax.set_ylim(-len(circuit.get_circuit()), 1)
    ax.set_xticks(range(circuit.num_qubits))
    ax.set_xticklabels([f'Q{i}' for i in range(circuit.num_qubits)])
    ax.grid(False)

    # Add a grid for better visualization
    ax.axhline(0, color='black', linewidth=0.5, linestyle='--')
    ax.axvline(0, color='black', linewidth=0.5, linestyle='--')

    plt.tight_layout()
    plt.show()

def visualize_gate(gate, qubit_index):
    """Visualizes a single quantum gate.
    
    Args:
        gate (np.ndarray): The unitary matrix representing the gate.
        qubit_index (int): The index of the qubit the gate acts on.
    """
    fig, ax = plt.subplots(figsize=(4, 2))
    ax.matshow(np.abs(gate), cmap='viridis', alpha=0.8)
    ax.set_title(f'Gate Visualization for Qubit {qubit_index}')
    ax.set_xticks([])
    ax.set_yticks([])
    for (i, j), val in np.ndenumerate(gate):
        ax.text(j, i, f'{val:.2f}', ha='center', va='center', color='white')
    plt.show()

# Example usage
if __name__ == "__main__":
    from .circuit import QuantumCircuit

    circuit = QuantumCircuit(2)
    x_gate = np.array([[0, 1], [1, 0]])  # X gate
    h_gate = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]])  # Hadamard gate
    circuit.add_gate(x_gate, [0])
    circuit.add_gate(h_gate, [1])
    
    visualize_circuit(circuit)
    
    # Visualize a specific gate
    visualize_gate(x_gate, 0)

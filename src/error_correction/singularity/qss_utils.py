### Updated `qss_utils.py`

"""
Utility functions for the Quantum Singularity Shield (QSS).
This module provides functions for data preprocessing, error handling,
and managing quantum states in the context of singularity-resilient quantum error correction.
"""

import numpy as np
from qiskit import QuantumCircuit

def preprocess_data(data: np.ndarray) -> np.ndarray:
    """
    Preprocess the input data for anomaly detection or quantum state preparation.

    Args:
        data (np.ndarray): The input data to preprocess.

    Returns:
        np.ndarray: The preprocessed data.
    """
    # Normalize data to the range [0, 1]
    min_val = np.min(data)
    max_val = np.max(data)
    normalized_data = (data - min_val) / (max_val - min_val)
    return normalized_data

def generate_random_quantum_state(num_qubits: int) -> np.ndarray:
    """
    Generate a random quantum state.

    Args:
        num_qubits (int): The number of qubits.

    Returns:
        np.ndarray: A normalized random quantum state.
    """
    state = np.random.rand(2**num_qubits) + 1j * np.random.rand(2**num_qubits)
    return state / np.linalg.norm(state)  # Normalize the state

def create_quantum_circuit(num_qubits: int) -> QuantumCircuit:
    """
    Create a quantum circuit with the specified number of qubits.

    Args:
        num_qubits (int): The number of qubits in the circuit.

    Returns:
        QuantumCircuit: The created quantum circuit.
    """
    return QuantumCircuit(num_qubits)

def apply_single_qubit_gate(circuit: QuantumCircuit, qubit_index: int, gate: str):
    """
    Apply a single-qubit gate to the specified qubit in the circuit.

    Args:
        circuit (QuantumCircuit): The quantum circuit.
        qubit_index (int): The index of the qubit to apply the gate to.
        gate (str): The name of the gate to apply (e.g., 'h', 'x', 'y', 'z').
    """
    if gate == 'h':
        circuit.h(qubit_index)
    elif gate == 'x':
        circuit.x(qubit_index)
    elif gate == 'y':
        circuit.y(qubit_index)
    elif gate == 'z':
        circuit.z(qubit_index)
    else:
        raise ValueError(f"Unsupported gate: {gate}")

def measure_qubits(circuit: QuantumCircuit, qubit_indices: list):
    """
    Measure the specified qubits in the circuit.

    Args:
        circuit (QuantumCircuit): The quantum circuit.
        qubit_indices (list): A list of indices of the qubits to measure.
    """
    for qubit_index in qubit_indices:
        circuit.measure(qubit_index, qubit_index)  # Measure and store in classical bit

def handle_error(error: Exception):
    """
    Handle errors that occur during quantum operations.

    Args:
        error (Exception): The error to handle.
    """
    print(f"An error occurred: {error}")

def visualize_quantum_state(state: np.ndarray):
    """
    Visualize the quantum state using a bar chart.

    Args:
        state (np.ndarray): The quantum state to visualize.
    """
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 5))
    plt.bar(range(len(state)), np.abs(state)**2, color='blue', alpha=0.7)
    plt.title("Quantum State Probability Distribution")
    plt.xlabel("Basis States")
    plt.ylabel("Probability Amplitude")
    plt.grid()
    plt.show()

# Example usage
if __name__ == "__main__":
    num_qubits = 3  # Example number of qubits

    # Generate a random quantum state
    random_state = generate_random_quantum_state(num_qubits)
    print("Random Quantum State:", random_state)

    # Create a quantum circuit
    circuit = create_quantum_circuit(num_qubits)

    # Apply gates
    apply_single_qubit_gate(circuit, 0, 'h')
    apply_single_qubit_gate(circuit, 1, 'x')

    # Measure qubits
    measure_qubits(circuit, [0, 1])

    # Visualize the quantum state
    visualize_quantum_state(random_state)

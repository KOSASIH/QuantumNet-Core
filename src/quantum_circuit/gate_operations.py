# quantum_circuit/gate_operations.py

import numpy as np
from .circuit import QuantumCircuit

def apply_gate(state, gate, qubit_index):
    """Applies a quantum gate to a specific qubit in the state.
    
    Args:
        state (np.ndarray): The state vector to which the gate is applied.
        gate (np.ndarray): The unitary matrix representing the gate.
        qubit_index (int): The index of the qubit to which the gate is applied.
    
    Returns:
        np.ndarray: The new state vector after applying the gate.
    
    Raises:
        ValueError: If the gate dimensions do not match the qubit index.
    """
    if gate.shape[0] != gate.shape[1] or gate.shape[0] != 2:
        raise ValueError("Gate must be a 2x2 unitary matrix.")
    
    # Create the full gate for the circuit
    full_gate = np.eye(1)
    for i in range(len(state)):
        if i == qubit_index:
            full_gate = np.kron(full_gate, gate)
        else:
            full_gate = np.kron(full_gate, np.eye(2))
    
    return np.dot(full_gate, state)

def apply_circuit(state, circuit):
    """Applies a series of gates in a quantum circuit to a state.
    
    Args:
        state (np.ndarray): The initial state vector.
        circuit (QuantumCircuit): The quantum circuit containing gates to apply.
    
    Returns:
        np.ndarray: The new state vector after applying the circuit.
    
    Raises:
        ValueError: If the circuit is empty or if the state dimensions do not match.
    """
    if not circuit.get_circuit():
        raise ValueError("The circuit is empty. No gates to apply.")
    
    for gate, qubits in circuit.get_circuit():
        for qubit in qubits:
            state = apply_gate(state, gate, qubit)
    
    return state

def apply_multiple_gates(state, gates_and_qubits):
    """Applies multiple gates to the state in sequence.
    
    Args:
        state (np.ndarray): The initial state vector.
        gates_and_qubits (list of tuples): A list of tuples where each tuple contains a gate and the corresponding qubit indices.
    
    Returns:
        np.ndarray: The new state vector after applying the gates.
    
    Raises:
        ValueError: If any gate dimensions do not match the qubit index.
    """
    for gate, qubit_index in gates_and_qubits:
        state = apply_gate(state, gate, qubit_index)
    return state

# Example usage
if __name__ == "__main__":
    state = np.array([1, 0])  # |0⟩ state
    x_gate = np.array([[0, 1], [1, 0]])  # X gate
    h_gate = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]])  # Hadamard gate

    # Apply X gate to the first qubit
    new_state = apply_gate(state, x_gate, 0)
    print("New State after applying X gate:", new_state)

    # Apply multiple gates
    combined_gates = [(x_gate, 0), (h_gate, 0)]  # Apply X gate and then Hadamard gate to the first qubit
    final_state = apply_multiple_gates(state, combined_gates)
    print("Final State after applying multiple gates:", final_state)

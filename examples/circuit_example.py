# examples/circuit_example.py

import numpy as np
from quantum_circuit.circuit import QuantumCircuit
from quantum_circuit.gate_operations import apply_circuit

def main():
    # Create a quantum circuit with 2 qubits
    circuit = QuantumCircuit(2)

    # Define gates
    x_gate = np.array([[0, 1], [1, 0]])  # X gate
    h_gate = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]])  # Hadamard gate

    # Add gates to the circuit
    circuit.add_gate(x_gate, [0])  # Apply X gate to qubit 0
    circuit.add_gate(h_gate, [1])   # Apply Hadamard gate to qubit 1

    # Initial state |00⟩
    initial_state = np.array([1, 0, 0, 0])  # |00⟩ state

    # Apply the circuit to the initial state
    final_state = apply_circuit(initial_state, circuit)
    print("Final state after applying the circuit:")
    print(final_state)

if __name__ == "__main__":
    main()

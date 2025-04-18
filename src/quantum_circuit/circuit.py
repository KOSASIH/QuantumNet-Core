# quantum_circuit/circuit.py

import numpy as np

class QuantumCircuit:
    """Class representing a quantum circuit."""
    
    def __init__(self, num_qubits):
        """Initializes the quantum circuit with a specified number of qubits.
        
        Args:
            num_qubits (int): The number of qubits in the circuit.
        """
        self.num_qubits = num_qubits
        self.gates = []  # List to store applied gates

    def add_gate(self, gate, qubits):
        """Adds a quantum gate to the circuit.
        
        Args:
            gate (np.ndarray): The unitary matrix representing the gate.
            qubits (list): The list of qubit indices the gate acts on.
        
        Raises:
            ValueError: If the gate does not match the number of qubits.
        """
        if not isinstance(gate, np.ndarray):
            raise ValueError("Gate must be a numpy array.")
        if len(qubits) != gate.shape[0].bit_length() - 1:
            raise ValueError("The number of qubits must match the gate dimensions.")
        
        self.gates.append((gate, qubits))

    def get_circuit(self):
        """Returns the list of gates in the circuit.
        
        Returns:
            list: The gates applied in the circuit.
        """
        return self.gates

    def apply(self, state):
        """Applies the entire circuit to a given quantum state.
        
        Args:
            state (np.ndarray): The initial state vector to apply the circuit to.
        
        Returns:
            np.ndarray: The resulting state vector after applying the circuit.
        """
        for gate, qubits in self.gates:
            state = self.apply_gate(state, gate, qubits)
        return state

    def apply_gate(self, state, gate, qubits):
        """Applies a quantum gate to a specific qubit in the state.
        
        Args:
            state (np.ndarray): The state vector to which the gate is applied.
            gate (np.ndarray): The unitary matrix representing the gate.
            qubits (list): The list of qubit indices the gate acts on.
        
        Returns:
            np.ndarray: The new state vector after applying the gate.
        """
        # Create the full gate for the circuit
        full_gate = np.eye(1)
        for i in range(self.num_qubits):
            if i in qubits:
                full_gate = np.kron(full_gate, gate)
            else:
                full_gate = np.kron(full_gate, np.eye(2))
        
        return np.dot(full_gate, state)

    def __repr__(self):
        return f"QuantumCircuit(num_qubits={self.num_qubits}, gates={self.gates})"

# Example usage
if __name__ == "__main__":
    circuit = QuantumCircuit(2)
    x_gate = np.array([[0, 1], [1, 0]])  # X gate
    h_gate = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]])  # Hadamard gate

    circuit.add_gate(x_gate, [0])  # Apply X gate to qubit 0
    circuit.add_gate(h_gate, [1])   # Apply Hadamard gate to qubit 1

    print(circuit)

    initial_state = np.array([1, 0, 0, 0])  # |00⟩ state
    final_state = circuit.apply(initial_state)
    print("Final State after applying circuit:", final_state)

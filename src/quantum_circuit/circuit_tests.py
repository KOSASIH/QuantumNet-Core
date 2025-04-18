# quantum_circuit/circuit_tests.py

import unittest
import numpy as np
from .circuit import QuantumCircuit
from .gate_operations import apply_gate, apply_circuit

class TestQuantumCircuit(unittest.TestCase):

    def test_quantum_circuit_creation(self):
        """Test the creation of a quantum circuit."""
        circuit = QuantumCircuit(2)
        self.assertEqual(circuit.num_qubits, 2)
        self.assertEqual(circuit.get_circuit(), [])

    def test_add_gate(self):
        """Test adding a gate to the quantum circuit."""
        circuit = QuantumCircuit(2)
        gate = np.array([[0, 1], [1, 0]])  # X gate
        circuit.add_gate(gate, [0])
        self.assertEqual(len(circuit.get_circuit()), 1)
        self.assertEqual(circuit.get_circuit()[0], (gate, [0]))

    def test_add_invalid_gate(self):
        """Test adding an invalid gate to the quantum circuit."""
        circuit = QuantumCircuit(2)
        invalid_gate = np.array([[1, 0], [0, 1], [0, 0]])  # Invalid 3x2 gate
        with self.assertRaises(ValueError):
            circuit.add_gate(invalid_gate, [0])

    def test_apply_gate(self):
        """Test applying a gate to a quantum state."""
        state = np.array([1, 0])  # |0⟩ state
        gate = np.array([[0, 1], [1, 0]])  # X gate
        new_state = apply_gate(state, gate, 0)
        self.assertTrue(np.array_equal(new_state, np.array([0, 1])))  # Should be |1⟩ state

    def test_apply_gate_invalid(self):
        """Test applying an invalid gate to a quantum state."""
        state = np.array([1, 0])  # |0⟩ state
        invalid_gate = np.array([[1, 0], [0, 1], [0, 0]])  # Invalid 3x2 gate
        with self.assertRaises(ValueError):
            apply_gate(state, invalid_gate, 0)

    def test_apply_circuit(self):
        """Test applying a series of gates in a quantum circuit."""
        circuit = QuantumCircuit(2)
        gate_x = np.array([[0, 1], [1, 0]])  # X gate
        gate_h = (1/np.sqrt(2)) * np.array([[1, 1], [1, -1]])  # Hadamard gate
        circuit.add_gate(gate_x, [0])
        circuit.add_gate(gate_h, [1])
        
        initial_state = np.array([1, 0, 0, 0])  # |00⟩ state
        final_state = apply_circuit(initial_state, circuit)
        expected_state = (1/2) * np.array([0, 1, 1, -1])  # Expected state after applying gates
        self.assertTrue(np.allclose(final_state, expected_state))

    def test_apply_empty_circuit(self):
        """Test applying an empty circuit to a state."""
        circuit = QuantumCircuit(2)
        initial_state = np.array([1, 0, 0, 0])  # |00⟩ state
        final_state = apply_circuit(initial_state, circuit)
        self.assertTrue(np.array_equal(final_state, initial_state))  # Should remain unchanged

if __name__ == "__main__":
    unittest.main()

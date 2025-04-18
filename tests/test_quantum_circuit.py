# tests/test_quantum_circuit.py

import unittest
import numpy as np
from quantum_circuit.circuit import QuantumCircuit
from quantum_circuit.gate_operations import apply_gate, apply_circuit

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

    def test_apply_circuit(self):
        """Test applying a series of gates in a quantum circuit."""
        circuit = QuantumCircuit(2)
        gate_x = np.array([[0, 1], [1, 0]])  # X gate
        circuit.add_gate(gate_x, [0])
        
        initial_state = np.array([1, 0, 0, 0])  # |00⟩ state
        final_state = apply_circuit(initial_state, circuit)
        expected_state = np.array([0, 1, 0, 0])  # Expected state after applying X gate
        self.assertTrue(np.array_equal(final_state, expected_state))

if __name__ == "__main__":
    unittest.main()

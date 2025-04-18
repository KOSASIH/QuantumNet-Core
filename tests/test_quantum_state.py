# tests/test_quantum_state.py

import unittest
import numpy as np
from quantum_circuit.quantum_state import apply_gate_to_state

class TestQuantumState(unittest.TestCase):

    def test_apply_gate_to_state(self):
        """Test applying a gate to a quantum state."""
        state = np.array([1, 0])  # |0⟩ state
        gate = np.array([[0, 1], [1, 0]])  # X gate
        new_state = apply_gate_to_state(state, gate)
        self.assertTrue(np.array_equal(new_state, np.array([0, 1])))  # Should be |1⟩ state

if __name__ == "__main__":
    unittest.main()

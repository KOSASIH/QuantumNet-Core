# tests/test_entanglement.py

import unittest
import numpy as np
from quantum_circuit.entanglement import create_entangled_state

class TestEntanglement(unittest.TestCase):

    def test_create_entangled_state(self):
        """Test the creation of a Bell state."""
        state = create_entangled_state()
        expected_state = np.array([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)])  # |00⟩ + |11⟩
        self.assertTrue(np.allclose(state, expected_state))

    def test_entangled_state_properties(self):
        """Test properties of the entangled state."""
        state = create_entangled_state()
        # Check normalization
        self.assertAlmostEqual(np.linalg.norm(state), 1)

if __name__ == "__main__":
    unittest.main()

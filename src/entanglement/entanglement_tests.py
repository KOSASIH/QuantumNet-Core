# entanglement/entanglement_tests.py

import unittest
import numpy as np
from .entangler import create_entangled_pair, measure_entanglement, QuantumState
from .entanglement_utils import normalize_state, fidelity, tensor_product, is_orthogonal

class TestEntanglement(unittest.TestCase):

    def test_create_entangled_pair(self):
        """Test the creation of an entangled pair of qubits."""
        qubit1, qubit2 = create_entangled_pair()
        self.assertEqual(len(qubit1.amplitudes), 4)
        self.assertEqual(len(qubit2.amplitudes), 4)
        self.assertTrue(np.isclose(np.linalg.norm(qubit1.amplitudes), 1))
        self.assertTrue(np.isclose(np.linalg.norm(qubit2.amplitudes), 1))

    def test_measure_entanglement(self):
        """Test the measurement of entanglement between two qubits."""
        qubit1, qubit2 = create_entangled_pair()
        entanglement_degree = measure_entanglement(qubit1, qubit2)
        self.assertGreaterEqual(entanglement_degree, 0)
        self.assertLessEqual(entanglement_degree, 1)  # Entanglement degree should be between 0 and 1

    def test_normalize_state(self):
        """Test the normalization of a quantum state."""
        state = np.array([1, 2, 3])
        normalized_state = normalize_state(state)
        self.assertAlmostEqual(np.linalg.norm(normalized_state), 1)

    def test_fidelity(self):
        """Test the fidelity calculation between two quantum states."""
        state1 = QuantumState([1, 0, 0, 0])  # |0⟩ state
        state2 = QuantumState([0, 1, 0, 0])  # |1⟩ state
        state3 = QuantumState([1/np.sqrt(2), 1/np.sqrt(2), 0, 0])  # |+⟩ state

        self.assertAlmostEqual(fidelity(state1.amplitudes, state2.amplitudes), 0)
        self.assertAlmostEqual(fidelity(state1.amplitudes, state3.amplitudes), 0.5)

    def test_tensor_product(self):
        """Test the tensor product of two quantum states."""
        state1 = QuantumState([1, 0])  # |0⟩
        state2 = QuantumState([0, 1])  # |1⟩
        tensor_result = tensor_product(state1.amplitudes, state2.amplitudes)
        expected_result = np.array([0, 1, 0, 0])  # |01⟩ state
        np.testing.assert_array_almost_equal(tensor_result, expected_result)

    def test_is_orthogonal(self):
        """Test the orthogonality check between two quantum states."""
        state1 = QuantumState([1, 0, 0, 0])  # |0⟩
        state2 = QuantumState([0, 1, 0, 0])  # |1⟩
        state3 = QuantumState([1, 1, 0, 0])  # |+⟩

        self.assertTrue(is_orthogonal(state1.amplitudes, state2.amplitudes))
        self.assertFalse(is_orthogonal(state1.amplitudes, state3.amplitudes))

if __name__ == '__main__':
    unittest.main()

# quantum_state/state_tests.py

import unittest
import numpy as np
from .state_vector import StateVector
from .density_matrix import DensityMatrix

class TestQuantumState(unittest.TestCase):

    def test_state_vector_creation(self):
        """Test the creation and normalization of a state vector."""
        state = StateVector([1, 2, 3])
        self.assertEqual(len(state.amplitudes), 3)
        self.assertAlmostEqual(np.linalg.norm(state.amplitudes), 1, places=7)

    def test_state_vector_measurement(self):
        """Test the measurement of a state vector."""
        state = StateVector([1, 0, 0])  # |0⟩ state
        measurement_result = state.measure()
        self.assertEqual(measurement_result, 0)

    def test_state_vector_inner_product(self):
        """Test the inner product calculation between two state vectors."""
        state1 = StateVector([1, 0, 0])  # |0⟩ state
        state2 = StateVector([0, 1, 0])  # |1⟩ state
        inner_prod = state1.inner_product(state2)
        self.assertEqual(inner_prod, 0)

        state3 = StateVector([1/np.sqrt(2), 1/np.sqrt(2)])  # |+⟩ state
        inner_prod2 = state1.inner_product(state3)
        self.assertAlmostEqual(inner_prod2, 1/np.sqrt(2), places=7)

    def test_state_vector_tensor_product(self):
        """Test the tensor product calculation between two state vectors."""
        state1 = StateVector([1, 0])  # |0⟩
        state2 = StateVector([0, 1])  # |1⟩
        tensor_result = state1.tensor_product(state2)
        expected_result = np.array([0, 1, 0, 0])  # |01⟩ state
        np.testing.assert_array_almost_equal(tensor_result.amplitudes, expected_result)

    def test_density_matrix_creation(self):
        """Test the creation and validation of a density matrix."""
        density_matrix = DensityMatrix([[1, 0], [0, 0]])  # |0⟩ state
        self.assertEqual(density_matrix.trace(), 1)

    def test_density_matrix_measurement(self):
        """Test the measurement of a density matrix."""
        density_matrix = DensityMatrix([[1, 0], [0, 0]])  # |0⟩ state
        measurement_result = density_matrix.measure()
        self.assertEqual(measurement_result, 0)

    def test_density_matrix_partial_trace(self):
        """Test the partial trace calculation of a density matrix."""
        combined_density_matrix = DensityMatrix([[1, 0, 0, 0], 
                                                  [0, 0, 0, 0], 
                                                  [0, 0, 0, 0], 
                                                  [0, 0, 0, 1]])  # |00⟩ + |11⟩
        reduced_density_matrix = combined_density_matrix.partial_trace(0)  # Trace out subsystem 0
        expected_result = DensityMatrix([[0.5, 0], 
                                          [0, 0.5]])  # Reduced density matrix for subsystem 1
        np.testing.assert_array_almost_equal(reduced_density_matrix.matrix, expected_result.matrix)

if __name__ == "__main__":
    unittest.main()

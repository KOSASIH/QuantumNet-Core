import unittest
import numpy as np
from mes_utils import (
    prepare_state_vector,
    normalize_state,
    compute_density_matrix,
    fidelity,
    entanglement_entropy,
    swap_entangled_states
)
from mes_visualization import visualize_state_on_bloch_sphere, visualize_density_matrix

class TestMESUtils(unittest.TestCase):

    def test_prepare_state_vector(self):
        """Test the preparation of a state vector from a binary string."""
        num_qubits = 3
        state = '101'
        expected_vector = np.array([0, 0, 1, 0, 0, 0, 0, 0])
        result_vector = prepare_state_vector(num_qubits, state)
        np.testing.assert_array_equal(result_vector, expected_vector)

    def test_normalize_state(self):
        """Test normalization of a state vector."""
        state_vector = np.array([1, 2, 2])
        normalized_vector = normalize_state(state_vector)
        expected_norm = 1.0
        self.assertAlmostEqual(np.linalg.norm(normalized_vector), expected_norm)

    def test_compute_density_matrix(self):
        """Test the computation of a density matrix."""
        state_vector = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
        density_matrix = compute_density_matrix(state_vector)
        expected_density_matrix = np.array([[0.5, 0.5], [0.5, 0.5]])
        np.testing.assert_array_almost_equal(density_matrix, expected_density_matrix)

    def test_fidelity(self):
        """Test the fidelity calculation between two quantum states."""
        state1 = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
        state2 = np.array([1/np.sqrt(2), -1/np.sqrt(2)])
        fidelity_value = fidelity(state1, state2)
        expected_fidelity = 0.0  # Orthogonal states
        self.assertAlmostEqual(fidelity_value, expected_fidelity)

    def test_entanglement_entropy(self):
        """Test the calculation of entanglement entropy."""
        state_vector = np.array([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)])  # Bell state
        density_matrix = compute_density_matrix(state_vector)
        entropy = entanglement_entropy(density_matrix)
        expected_entropy = 1.0  # Bell state has maximum entanglement
        self.assertAlmostEqual(entropy, expected_entropy)

    def test_swap_entangled_states(self):
        """Test the swapping of two entangled states."""
        state1 = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
        state2 = np.array([0, 1])
        swapped_state1, swapped_state2 = swap_entangled_states(state1, state2)
        np.testing.assert_array_equal(swapped_state1, state2)
        np.testing.assert_array_equal(swapped_state2, state1)

# Note: Visualization functions are typically not tested in unit tests
# as they produce graphical output. However, you can check if they run without errors.

class TestMESVisualization(unittest.TestCase):

    def test_visualize_state_on_bloch_sphere(self):
        """Test if the Bloch sphere visualization function runs without errors."""
        state_vector = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
        try:
            visualize_state_on_bloch_sphere(state_vector)
        except Exception as e:
            self.fail(f"visualize_state_on_bloch_sphere raised an exception: {e}")

    def test_visualize_density_matrix(self):
        """Test if the density matrix visualization function runs without errors."""
        state_vector = np.array([1/np.sqrt(2), 1/np.sqrt(2)])
        density_matrix = compute_density_matrix(state_vector)
        try:
            visualize_density_matrix(density_matrix)
        except Exception as e:
            self.fail(f"visualize_density_matrix raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()

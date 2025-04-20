import unittest
import numpy as np
from qiskit.quantum_info import Statevector
from cnre_utils import (
    apply_noise,
    calculate_fidelity,
    generate_noisy_states,
    preprocess_data
)
from cnre_visualization import visualize_state, compare_states

class TestCNREUtils(unittest.TestCase):
    def setUp(self):
        """Set up test variables."""
        self.original_state = Statevector.from_dict({'00': 1, '01': 0, '10': 0, '11': 0})
        self.noise_level = 0.1
        self.noisy_state = apply_noise(self.original_state, 'depolarizing', self.noise_level)

    def test_apply_noise(self):
        """Test the application of noise to a quantum state."""
        self.assertIsInstance(self.noisy_state, Statevector)
        self.assertNotEqual(self.original_state, self.noisy_state)

    def test_calculate_fidelity(self):
        """Test the fidelity calculation between two states."""
        fidelity = calculate_fidelity(self.original_state, self.noisy_state)
        self.assertGreaterEqual(fidelity, 0)
        self.assertLessEqual(fidelity, 1)

    def test_generate_noisy_states(self):
        """Test the generation of noisy states from original states."""
        original_states = np.array([self.original_state.data])
        noisy_states = generate_noisy_states(original_states, 'bit_flip', self.noise_level)
        self.assertEqual(len(noisy_states), 1)
        self.assertIsInstance(noisy_states[0], Statevector)

    def test_preprocess_data(self):
        """Test the preprocessing of data."""
        raw_data = np.array([1, 2, 3])
        preprocessed_data = preprocess_data(raw_data)
        self.assertAlmostEqual(np.linalg.norm(preprocessed_data), 1.0)

class TestCNREVisualization(unittest.TestCase):
    def setUp(self):
        """Set up test variables for visualization."""
        self.original_state = Statevector.from_dict({'00': 1, '01': 0, '10': 0, '11': 0})
        self.noisy_state = apply_noise(self.original_state, 'depolarizing', 0.1)

    def test_visualize_state(self):
        """Test the visualization of a quantum state."""
        try:
            visualize_state(self.original_state)
            visualize_state(self.noisy_state)
        except Exception as e:
            self.fail(f"Visualization failed with exception: {e}")

    def test_compare_states(self):
        """Test the comparison of original and noisy states."""
        try:
            compare_states(self.original_state, self.noisy_state)
        except Exception as e:
            self.fail(f"Comparison visualization failed with exception: {e}")

if __name__ == '__main__':
    unittest.main()

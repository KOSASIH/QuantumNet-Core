"""
Unit tests for Autonomous Quantum Civilization Synthesizer (AQCS) utilities.
"""
import unittest
import numpy as np
from aqcs_utils import (
    calculate_average_state,
    normalize_states,
    calculate_entropy,
)

class TestAQCSUtils(unittest.TestCase):

    def setUp(self):
        """Set up test data."""
        self.agent_states = np.array([0, 1, 2, 3, 4, 5])
        self.agent_states_with_zeros = np.array([0, 0, 0, 0, 0])
        self.random_states = np.random.rand(100)

    def test_calculate_average_state(self):
        """Test average state calculation."""
        average = calculate_average_state(self.agent_states)
        self.assertAlmostEqual(average, 2.5)

    def test_normalize_states(self):
        """Test normalization of states."""
        normalized = normalize_states(self.agent_states)
        self.assertTrue(np.all(normalized >= 0) and np.all(normalized <= 1))
        normalized_zeros = normalize_states(self.agent_states_with_zeros)
        self.assertTrue(np.all(normalized_zeros == 0))

    def test_calculate_entropy(self):
        """Test entropy calculation."""
        entropy = calculate_entropy(self.agent_states)
        self.assertGreater(entropy, 0)

    def test_entropy_with_uniform_distribution(self):
        """Test entropy for uniform distribution."""
        uniform_states = np.array([1, 1, 1, 1])
        entropy = calculate_entropy(uniform_states)
        self.assertEqual(entropy, 0)

if __name__ == "__main__":
    unittest.main()

# src/qnn/qnn_tests.py

import unittest
import numpy as np
from unittest.mock import patch
from state_predictor import QuantumStatePredictor
from qnn_utils import preprocess_data, postprocess_results, data_augmentation

class TestQuantumStatePredictor(unittest.TestCase):
    
    def setUp(self):
        self.predictor = QuantumStatePredictor(num_qubits=2)

    @patch('state_predictor.execute')
    def test_predict(self, mock_execute):
        # Mock the execution result
        mock_execute.return_value.result.return_value.get_statevector.return_value = np.array([1, 0, 0, 0])
        
        parameters = np.array([0.5, 0.5])
        statevector = self.predictor.predict(parameters)
        self.assertEqual(len(statevector), 4)  # 2 qubits -> 4 states
        self.assertTrue(np.all(np.isreal(statevector)))  # Ensure the statevector is real

    @patch('state_predictor.execute')
    def test_evaluate(self, mock_execute):
        # Mock the execution result
        mock_execute.return_value.result.return_value.get_statevector.return_value = np.array([1, 0, 0, 0])
        
        parameters = np.array([0.5, 0.5])
        probabilities = self.predictor.evaluate(parameters)
        self.assertAlmostEqual(sum(probabilities), 1.0)  # Probabilities should sum to 1
        self.assertTrue(np.all(probabilities >= 0))  # Probabilities should be non-negative

    def test_preprocess_data_min_max(self):
        data = np.array([1, 2, 3, 4, 5])
        normalized_data = preprocess_data(data, method='min-max')
        self.assertTrue(np.all(normalized_data >= 0) and np.all(normalized_data <= 1))

    def test_preprocess_data_z_score(self):
        data = np.array([1, 2, 3, 4, 5])
        normalized_data = preprocess_data(data, method='z-score')
        self.assertAlmostEqual(np.mean(normalized_data), 0, delta=0.1)  # Mean should be close to 0
        self.assertAlmostEqual(np.std(normalized_data), 1, delta=0.1)  # Std should be close to 1

    def test_postprocess_results(self):
        results = np.array([0.1, 0.3, 0.4, 0.2])
        processed = postprocess_results(results)
        self.assertEqual(len(processed), 4)  # Should match the number of states
        self.assertEqual(processed['State 0'], 0.1)  # Check specific state probability

    def test_data_augmentation(self):
        data = np.array([1, 2, 3, 4, 5])
        augmented_data = data_augmentation(data, factor=0.5)
        self.assertEqual(data.shape, augmented_data.shape)  # Shape should remain the same
        self.assertTrue(np.all(augmented_data >= 0))  # Ensure no negative values

if __name__ == "__main__":
    unittest.main()

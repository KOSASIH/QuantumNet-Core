import unittest
import numpy as np
from src.qml.entanglement_optimizer import EntanglementOptimizer
from src.qml.qml_utils import normalize_data, transform_data, prepare_data_for_training, generate_random_quantum_state
from src.qml.qml_visualization import plot_bloch_sphere, plot_training_results, plot_histogram

class TestQMLFunctions(unittest.TestCase):

    def setUp(self):
        """Set up test variables."""
        self.optimizer = EntanglementOptimizer(num_qubits=2)
        self.test_state = np.array([1/np.sqrt(2), 1/np.sqrt(2)])  # Example quantum state
        self.test_data = np.array([1, 2, 3, 4, 5])
        self.transformation_matrix = np.array([[0, 1], [1, 0]])  # Simple swap matrix

    def test_normalize_data(self):
        """Test the normalization of quantum data."""
        normalized = normalize_data(self.test_data)
        self.assertAlmostEqual(np.linalg.norm(normalized), 1.0, places=5)

    def test_transform_data(self):
        """Test the transformation of quantum data."""
        transformed = transform_data(self.test_state, self.transformation_matrix)
        expected = np.array([1/np.sqrt(2), 1/np.sqrt(2)])  # After transformation, it should be the same
        np.testing.assert_array_almost_equal(transformed, expected)

    def test_prepare_data_for_training(self):
        """Test the preparation of data for training."""
        prepared_data = prepare_data_for_training(self.test_data)
        self.assertAlmostEqual(np.linalg.norm(prepared_data), 1.0, places=5)

    def test_generate_random_quantum_state(self):
        """Test the generation of a random quantum state."""
        random_state = generate_random_quantum_state(2)
        self.assertEqual(random_state.shape[0], 4)  # For 2 qubits, the state vector should have 4 elements
        self.assertAlmostEqual(np.linalg.norm(random_state), 1.0, places=5)

    def test_optimize_entanglement(self):
        """Test the entanglement optimization process."""
        initial_params = [0.0, 0.0]
        result = self.optimizer.optimize_entanglement(initial_params)
        self.assertIsNotNone(result)  # Ensure that the optimization returns a result

    def test_plot_bloch_sphere(self):
        """Test the Bloch sphere plotting function."""
        try:
            plot_bloch_sphere(self.test_state)  # This should not raise an error
        except Exception as e:
            self.fail(f"plot_bloch_sphere raised an exception: {e}")

    def test_plot_training_results(self):
        """Test the training results plotting function."""
        epochs = list(range(1, 11))
        accuracy = [0.1, 0.3, 0.5, 0.6, 0.7, 0.8, 0.85, 0.9, 0.95, 1.0]
        loss = [1.0, 0.9, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.01]
        try:
            plot_training_results(epochs, accuracy, loss)  # This should not raise an error
        except Exception as e:
            self.fail(f"plot_training_results raised an exception: {e}")

    def test_plot_histogram(self):
        """Test the histogram plotting function."""
        data = np.random.normal(0, 1, 1000)
        try:
            plot_histogram(data)  # This should not raise an error
        except Exception as e:
            self.fail(f"plot_histogram raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()

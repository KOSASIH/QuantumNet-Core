import unittest
import numpy as np
from qgrm_utils import (
    load_data,
    preprocess_data,
    split_data,
    evaluate_model,
    save_results,
    normalize_data
)
from gravity_simulator import GravitySimulator
from qve_gravity_model import QVEGravityModel
from qnn_gravity_predictor import QNNGravityPredictor

class TestQGRMUtils(unittest.TestCase):
    def test_load_data(self):
        """Test loading data from a JSON file."""
        # Assuming 'test_data.json' is a valid JSON file with appropriate structure
        df = load_data('test_data.json')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertGreater(len(df), 0)

    def test_preprocess_data(self):
        """Test preprocessing of data."""
        df = load_data('test_data.json')
        X, y = preprocess_data(df, target_column='target')
        self.assertEqual(X.shape[0], len(y))
        self.assertEqual(X.shape[1], df.shape[1] - 1)

    def test_split_data(self):
        """Test splitting data into training and testing sets."""
        X = np.random.rand(100, 5)
        y = np.random.randint(0, 2, size=100)
        X_train, X_test, y_train, y_test = split_data(X, y)
        self.assertEqual(X_train.shape[0] + X_test.shape[0], 100)

    def test_evaluate_model_regression(self):
        """Test evaluation metrics for regression."""
        y_true = np.array([3, -0.5, 2, 7])
        y_pred = np.array([2.5, 0.0, 2, 8])
        metrics = evaluate_model(y_true, y_pred, model_type='regression')
        self.assertIn('mse', metrics)
        self.assertIn('rmse', metrics)

    def test_evaluate_model_classification(self):
        """Test evaluation metrics for classification."""
        y_true = np.array([1, 0, 1, 1])
        y_pred = np.array([1, 0, 0, 1])
        metrics = evaluate_model(y_true, y_pred, model_type='classification')
        self.assertIn('accuracy', metrics)

    def test_normalize_data(self):
        """Test normalization of data."""
        X = np.array([[1, 2], [2, 3], [3, 4]])
        X_normalized = normalize_data(X)
        self.assertTrue(np.all(X_normalized >= 0) and np.all(X_normalized <= 1))

class TestGravitySimulator(unittest.TestCase):
    def setUp(self):
        """Set up the Gravity Simulator for testing."""
        self.simulator = GravitySimulator(n_qubits=3)

    def test_generate_gravitational_field(self):
        """Test generation of a random gravitational field."""
        gravity_field = self.simulator.generate_gravitational_field(3)
        self.assertEqual(gravity_field.shape[0], 3)

    def test_build_circuit(self):
        """Test building a quantum circuit based on gravitational field."""
        gravity_field = np.array([0.5, -0.3, 0.2])
        circuit = self.simulator.build_circuit(gravity_field)
        self.assertEqual(circuit.num_qubits, 3)

    def test_simulate(self):
        """Test simulation of the quantum circuit."""
        gravity_field = np.array([0.5, -0.3, 0.2])
        results = self.simulator.simulate(gravity_field, shots=1024)
        self.assertIsInstance(results, dict)

class TestQVEGravityModel(unittest.TestCase):
    def setUp(self):
        """Set up the QVE Gravity Model for testing."""
        self.model = QVEGravityModel(n_qubits=3)

    def test_build_hamiltonian(self):
        """Test Hamiltonian construction based on gravitational field."""
        gravity_field = np.array([0.5, -0.3, 0.2])
        hamiltonian = self.model.build_hamiltonian(gravity_field)
        self.assertEqual(len(hamiltonian), 3)

    def test_optimize(self):
        """Test optimization of the circuit."""
        gravity_field = np.array([0.5, -0.3, 0.2])
        eigenvalue = self.model.optimize(gravity_field, max_iter=10)
        self.assertIsInstance(eigenvalue, float)

 def test_predict(self):
        """Test prediction capability of the model."""
        gravity_field = np.array([0.5, -0.3, 0.2])
        prediction = self.model.predict(gravity_field)
        self.assertIsInstance(prediction, np.ndarray)

class TestQNNGravityPredictor(unittest.TestCase):
    def setUp(self):
        """Set up the QNN Gravity Predictor for testing."""
        self.predictor = QNNGravityPredictor(n_qubits=3)

    def test_train(self):
        """Test training of the quantum neural network."""
        X_train = np.random.rand(100, 3)
        y_train = np.random.randint(0, 2, size=100)
        self.predictor.train(X_train, y_train)
        self.assertTrue(self.predictor.is_trained)

    def test_predict(self):
        """Test prediction from the trained model."""
        X_test = np.random.rand(10, 3)
        predictions = self.predictor.predict(X_test)
        self.assertEqual(predictions.shape[0], 10)

if __name__ == "__main__":
    unittest.main()

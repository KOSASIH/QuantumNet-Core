### `test_qnn.py`

import unittest
import numpy as np
from qiskit import Aer
from qiskit_machine_learning.algorithms import QNN
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

class TestQuantumNeuralNetwork(unittest.TestCase):

    def setUp(self):
        # Create a synthetic dataset for testing
        self.X, self.y = make_classification(n_samples=1000, n_features=10, n_classes=2, random_state=42)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2, random_state=42)

        # Standardize the data
        self.scaler = StandardScaler()
        self.X_train = self.scaler.fit_transform(self.X_train)
        self.X_test = self.scaler.transform(self.X_test)

        # Initialize the quantum neural network
        self.qnn = QNN(quantum_instance=Aer.get_backend('qasm_simulator'))

    def test_training(self):
        """Test if the model can be trained without errors."""
        self.qnn.fit(self.X_train, self.y_train)
        self.assertIsNotNone(self.qnn)

    def test_prediction(self):
        """Test if the model can make predictions."""
        self.qnn.fit(self.X_train, self.y_train)
        predictions = self.qnn.predict(self.X_test)
        self.assertEqual(len(predictions), len(self.y_test))

    def test_accuracy(self):
        """Test if the model achieves a reasonable accuracy."""
        self.qnn.fit(self.X_train, self.y_train)
        predictions = self.qnn.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, predictions)
        self.assertGreaterEqual(accuracy, 0.5)  # Expecting at least 50% accuracy

    def test_invalid_input(self):
        """Test if the model raises an error on invalid input."""
        with self.assertRaises(ValueError):
            self.qnn.fit(np.array([[1, 2], [3, 4]]), np.array([0, 1, 1]))  # Mismatched dimensions

    def test_model_persistence(self):
        """Test if the model can be saved and loaded correctly."""
        from qiskit_machine_learning.utils import save_model, load_model
        model_path = 'qnn_model.pkl'
        
        # Train the model
        self.qnn.fit(self.X_train, self.y_train)
        
        # Save the model
        save_model(self.qnn, model_path)
        
        # Load the model
        loaded_model = load_model(model_path)
        
        # Check if the loaded model can make predictions
        loaded_predictions = loaded_model.predict(self.X_test)
        self.assertEqual(len(loaded_predictions), len(self.y_test))

    def test_hyperparameter_tuning(self):
        """Test if hyperparameter tuning improves model performance."""
        from sklearn.model_selection import GridSearchCV
        
        param_grid = {
            'layers': [[2, 2], [3, 3]],  # Example layer configurations
            'activation': ['sigmoid', 'relu']
        }
        
        grid_search = GridSearchCV(QNN(quantum_instance=Aer.get_backend('qasm_simulator')), param_grid, cv=3)
        grid_search.fit(self.X_train, self.y_train)
        
        best_model = grid_search.best_estimator_
        best_accuracy = best_model.score(self.X_test, self.y_test)
        
        self.assertGreaterEqual(best_accuracy, 0.5)  # Expecting at least 50% accuracy

    def test_classification_report(self):
        """Test if the classification report can be generated correctly."""
        self.qnn.fit(self.X_train, self.y_train)
        predictions = self.qnn.predict(self.X_test)
        
        report = classification_report(self.y_test, predictions, output_dict=True)
        self.assertIn('0', report)  # Check if class '0' is in the report
        self.assertIn('1', report)  # Check if class '1' is in the report

if __name__ == '__main__':
    unittest.main()

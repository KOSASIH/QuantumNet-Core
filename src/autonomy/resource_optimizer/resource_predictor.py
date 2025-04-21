"""
Resource Predictor for Quantum Resource Hyper-Optimizer (QRHO).
"""
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

class ResourcePredictor:
    def __init__(self):
        """Initialize the resource predictor."""
        self.model = LinearRegression()
        self.is_trained = False

    def train(self, historical_data: np.ndarray, resource_usage: np.ndarray) -> None:
        """
        Train the resource prediction model.

        Parameters:
        historical_data (np.ndarray): Historical data features.
        resource_usage (np.ndarray): Historical resource usage data.
        """
        self.model.fit(historical_data, resource_usage)
        self.is_trained = True
        print("Model trained successfully.")

    def predict(self, new_data: np.ndarray) -> np.ndarray:
        """
        Predict future resource usage.

        Parameters:
        new_data (np.ndarray): New data for prediction.

        Returns:
        np.ndarray: Predicted resource usage.
        """
        if not self.is_trained:
            raise RuntimeError("Model must be trained before making predictions.")
        return self.model.predict(new_data)

    def evaluate(self, test_data: np.ndarray, test_usage: np.ndarray) -> float:
        """
        Evaluate the model's performance on test data.

        Parameters:
        test_data (np.ndarray): Test data features.
        test_usage (np.ndarray): Actual resource usage for test data.

        Returns:
        float: Mean squared error of the predictions.
        """
        predictions = self.predict(test_data)
        mse = mean_squared_error(test_usage, predictions)
        print(f"Mean Squared Error: {mse:.4f}")
        return mse

    def save_model(self, filename: str) -> None:
        """
        Save the trained model to a file.

        Parameters:
        filename (str): The name of the file to save the model.
        """
        joblib.dump(self.model, filename)
        print(f"Model saved to {filename}.")

    def load_model(self, filename: str) -> None:
        """
        Load a trained model from a file.

        Parameters:
        filename (str): The name of the file to load the model from.
        """
        self.model = joblib.load(filename)
        self.is_trained = True
        print(f"Model loaded from {filename}.")

# Example usage:
if __name__ == "__main__":
    # Sample historical data and resource usage
    historical_data = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
    resource_usage = np.array([1, 2, 3, 4])

    # Initialize and train the predictor
    predictor = ResourcePredictor()
    predictor.train(historical_data, resource_usage)

    # Predict future resource usage
    new_data = np.array([[5, 6]])
    prediction = predictor.predict(new_data)
    print("Predicted Resource Usage:", prediction)

    # Evaluate the model
    test_data = np.array([[5, 6], [6, 7]])
    test_usage = np.array([5, 6])
    predictor.evaluate(test_data, test_usage)

    # Save the model
    predictor.save_model("resource_predictor_model.pkl")

    # Load the model
    predictor.load_model("resource_predictor_model.pkl")

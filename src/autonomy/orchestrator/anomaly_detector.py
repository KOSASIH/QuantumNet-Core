import numpy as np
import logging
import pickle
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

class AnomalyDetector:
    def __init__(self, model=None):
        """Initialize the AnomalyDetector with a specified model or a default Isolation Forest model."""
        if model is None:
            self.model = IsolationForest(contamination=0.1)  # Default model
        else:
            self.model = model
        self.is_trained = False

        # Set up logging
        logging.basicConfig(level=logging.INFO)

    def train(self, data):
        """Train the anomaly detection model using the provided data."""
        logging.info("Training the anomaly detection model...")
        self.model.fit(data)
        self.is_trained = True
        logging.info("Model training completed.")

    def detect(self, data):
        """Detect anomalies in the provided data."""
        if not self.is_trained:
            logging.error("Model has not been trained yet. Please train the model before detection.")
            return None

        logging.info("Detecting anomalies...")
        predictions = self.model.predict(data)
        anomalies = data[predictions == -1]  # Anomalies are labeled as -1
        logging.info(f"Detected {len(anomalies)} anomalies.")
        return anomalies

    def set_contamination(self, contamination):
        """Set the contamination parameter for the model."""
        self.model.contamination = contamination
        logging.info(f"Contamination parameter set to {contamination}.")

    def visualize_anomalies(self, data, anomalies):
        """Visualize the detected anomalies in the data."""
        plt.figure(figsize=(10, 6))
        plt.scatter(data[:, 0], data[:, 1], label='Normal Data', color='blue')
        plt.scatter(anomalies[:, 0], anomalies[:, 1], label='Anomalies', color='red')
        plt.title("Anomaly Detection")
        plt.xlabel("Feature 1")
        plt.ylabel("Feature 2")
        plt.legend()
        plt.show()

    def save_model(self, filename):
        """Save the trained model to a file."""
        with open(filename, 'wb') as f:
            pickle.dump(self.model, f)
        logging.info(f"Model saved to {filename}.")

    def load_model(self, filename):
        """Load a trained model from a file."""
        with open(filename, 'rb') as f:
            self.model = pickle.load(f)
        self.is_trained = True
        logging.info(f"Model loaded from {filename}.")

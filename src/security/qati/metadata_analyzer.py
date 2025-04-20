"""
Metadata Analyzer using 3D ResNet for analyzing metadata.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MetadataAnalyzer:
    def __init__(self, input_shape, num_classes):
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.model = self.build_model()
        logging.info("3D ResNet model built successfully.")

    def build_model(self):
        """Builds a 3D ResNet model."""
        model = models.Sequential()
        model.add(layers.Conv3D(64, (3, 3, 3), activation='relu', input_shape=self.input_shape))
        model.add(layers.MaxPooling3D((2, 2, 2)))
        model.add(layers.Conv3D(128, (3, 3, 3), activation='relu'))
        model.add(layers.MaxPooling3D((2, 2, 2)))
        model.add(layers.Conv3D(256, (3, 3, 3), activation='relu'))
        model.add(layers.MaxPooling3D((2, 2, 2)))
        model.add(layers.Flatten())
        model.add(layers.Dense(512, activation='relu'))
        model.add(layers.Dense(self.num_classes, activation='softmax'))
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        return model

    def preprocess_data(self, metadata):
        """Preprocesses the metadata for analysis."""
        logging.info("Starting data preprocessing...")
        # Example preprocessing: Normalize and reshape data
        scaler = StandardScaler()
        metadata_scaled = scaler.fit_transform(metadata)
        metadata_reshaped = metadata_scaled.reshape((-1,) + self.input_shape)
        logging.info("Data preprocessing completed.")
        return metadata_reshaped

    def train_model(self, X, y, epochs=10, batch_size=32):
        """Trains the 3D ResNet model."""
        logging.info("Starting model training...")
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)
        history = self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_data=(X_val, y_val))
        logging.info("Model training completed.")
        return history

    def evaluate_model(self, X_test, y_test):
        """Evaluates the model on test data."""
        logging.info("Evaluating model...")
        test_loss, test_accuracy = self.model.evaluate(X_test, y_test)
        logging.info(f"Test Loss: {test_loss:.4f}, Test Accuracy: {test_accuracy:.4f}")
        return test_loss, test_accuracy

    def visualize_results(self, history):
        """Visualizes training results."""
        logging.info("Visualizing training results...")
        plt.figure(figsize=(12, 4))
        
        # Plot training & validation accuracy values
        plt.subplot(1, 2, 1)
        plt.plot(history.history['accuracy'], label='Train Accuracy')
        plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
        plt.title('Model Accuracy')
        plt.ylabel('Accuracy')
        plt.xlabel('Epoch')
        plt.legend(loc='upper left')

        # Plot training & validation loss values
        plt.subplot(1, 2, 2)
        plt.plot(history.history['loss'], label='Train Loss')
        plt.plot(history.history['val_loss'], label='Validation Loss')
        plt.title('Model Loss')
        plt.ylabel('Loss')
        plt.xlabel('Epoch')
        plt.legend(loc='upper left')

        plt.tight_layout()
        plt.show()
        logging.info("Visualization completed.")

# Example usage
if __name__ == "__main__":
    # Example metadata (replace with actual data)
    num_samples = 1000
    num_features = 30  # Example feature size
    num_classes = 5    # Example number of classes
    input_shape = (10, 10, 10, num_features)  # Example input shape for 3D data

    # Generate random metadata for demonstration
    metadata = np.random.rand(num_samples, num_features)
    labels = np.random.randint(0, num_classes , num_samples)  # Random labels for the classes

    analyzer = MetadataAnalyzer(input_shape, num_classes)
    preprocessed_data = analyzer.preprocess_data(metadata)
    history = analyzer.train_model(preprocessed_data, labels, epochs=20, batch_size=16)
    test_loss, test_accuracy = analyzer.evaluate_model(preprocessed_data, labels)
    analyzer.visualize_results(history)

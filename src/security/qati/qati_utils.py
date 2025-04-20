"""
Utility functions for Quantum Adversarial Threat Intelligence (QATI).
"""

import numpy as np
import pandas as pd
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_data(file_path):
    """
    Load data from a CSV file.

    Parameters:
    - file_path (str): Path to the CSV file.

    Returns:
    - pd.DataFrame: Loaded data as a pandas DataFrame.
    """
    if not os.path.exists(file_path):
        logging.error(f"File not found: {file_path}")
        raise FileNotFoundError(f"File not found: {file_path}")
    
    data = pd.read_csv(file_path)
    logging.info(f"Data loaded successfully from {file_path}.")
    return data

def preprocess_data(data, target_column):
    """
    Preprocess the data by separating features and target variable.

    Parameters:
    - data (pd.DataFrame): The input data.
    - target_column (str): The name of the target column.

    Returns:
    - X (np.ndarray): Features as a NumPy array.
    - y (np.ndarray): Target variable as a NumPy array.
    """
    X = data.drop(columns=[target_column]).values
    y = data[target_column].values
    logging.info("Data preprocessing completed.")
    return X, y

def split_data(X, y, test_size=0.2, random_state=42):
    """
    Split the data into training and testing sets.

    Parameters:
    - X (np.ndarray): Features.
    - y (np.ndarray): Target variable.
    - test_size (float): Proportion of the dataset to include in the test split.
    - random_state (int): Random seed for reproducibility.

    Returns:
    - X_train (np.ndarray): Training features.
    - X_test (np.ndarray): Testing features.
    - y_train (np.ndarray): Training target variable.
    - y_test (np.ndarray): Testing target variable.
    """
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    logging.info("Data split into training and testing sets.")
    return X_train, X_test, y_train, y_test

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the model on the test data.

    Parameters:
    - model: The trained model to evaluate.
    - X_test (np.ndarray): Testing features.
    - y_test (np.ndarray): Testing target variable.

    Returns:
    - accuracy (float): Accuracy of the model on the test data.
    """
    from sklearn.metrics import accuracy_score
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    logging.info(f"Model evaluation completed. Accuracy: {accuracy:.4f}")
    return accuracy

def save_model(model, filename):
    """
    Save the trained model to a file.

    Parameters:
    - model: The trained model to save.
    - filename (str): The filename to save the model.
    """
    import joblib
    joblib.dump(model, filename)
    logging.info(f"Model saved to {filename}.")

def load_model(filename):
    """
    Load a trained model from a file.

    Parameters:
    - filename (str): The filename to load the model from.

    Returns:
    - model: The loaded model.
    """
    import joblib
    model = joblib.load(filename)
    logging.info(f"Model loaded from {filename}.")
    return model

def visualize_results(history):
    """
    Visualize training results.

    Parameters:
    - history: The history object returned by the model's fit method.
    """
    import matplotlib.pyplot as plt

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
    logging.info("Results visualization completed.")

def log_model_parameters(model):
    """
    Log the parameters of the model.

    Parameters:
    - model: The model whose parameters are to be logged.
    """
    logging.info("Model parameters:")
    for layer in model.layers:
        logging.info(f"{layer.name}: {layer.count_params()} parameters")

def check_data_integrity(data):
    """
    Check the integrity of the data for missing values.

    Parameters:
    - data (pd.DataFrame): The input data.

    Returns:
    - bool: True if data is complete, False otherwise.
    """
    if data.isnull().values.any():
        logging.warning("Data contains missing values.")
        return False
    logging.info("Data integrity check passed.")
    return True

def normalize_data(X):
    """
    Normalize the feature data.

    Parameters:
    - X (np.ndarray): Features to normalize.

    Returns:
    - np.ndarray: Normalized features.
    """
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    X_normalized = scaler.fit_transform(X)
    logging.info("Data normalization completed.")
    return X_normalized

# Example usage
if __name__ == "__main__":
    # Example file path (replace with actual path)
    file_path = "data/qati_data.csv"
    
    try:
        data = load_data(file_path)
        if check_data_integrity(data):
            X, y = preprocess_data(data, target_column='target')
            X_train, X_test, y_train, y_test = split_data(X, y)
            # Assume 'model' is a pre-trained model
            accuracy = evaluate_model(model, X_test, y_test)
            logging.info(f"Model accuracy: {accuracy:.4f}")
            save_model(model, "qati_model.pkl")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

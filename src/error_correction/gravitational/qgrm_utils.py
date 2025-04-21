"""
Utility Functions for the Quantum Gravitational Resilience Module (QGRM)
"""
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, accuracy_score
from sklearn.model_selection import train_test_split
import json

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load data from a JSON file into a Pandas DataFrame.

    Parameters:
    file_path (str): Path to the JSON file containing the data.

    Returns:
    pd.DataFrame: DataFrame containing the loaded data.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return pd.DataFrame(data)

def preprocess_data(df: pd.DataFrame, target_column: str) -> (np.ndarray, np.ndarray):
    """
    Preprocess the data by separating features and target variable.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    target_column (str): The name of the target column.

    Returns:
    (np.ndarray, np.ndarray): Tuple containing features and target variable.
    """
    X = df.drop(columns=[target_column]).values
    y = df[target_column].values
    return X, y

def split_data(X: np.ndarray, y: np.ndarray, test_size: float = 0.2, random_state: int = 42) -> (np.ndarray, np.ndarray, np.ndarray, np.ndarray):
    """
    Split the data into training and testing sets.

    Parameters:
    X (np.ndarray): Features.
    y (np.ndarray): Target variable.
    test_size (float): Proportion of the dataset to include in the test split.
    random_state (int): Random seed for reproducibility.

    Returns:
    (np.ndarray, np.ndarray, np.ndarray, np.ndarray): Tuple containing training and testing sets.
    """
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def evaluate_model(y_true: np.ndarray, y_pred: np.ndarray, model_type: str = 'regression') -> dict:
    """
    Evaluate the model performance based on true and predicted values.

    Parameters:
    y_true (np.ndarray): True target values.
    y_pred (np.ndarray): Predicted target values.
    model_type (str): Type of model ('regression' or 'classification').

    Returns:
    dict: Dictionary containing evaluation metrics.
    """
    metrics = {}
    if model_type == 'regression':
        metrics['mse'] = mean_squared_error(y_true, y_pred)
        metrics['rmse'] = np.sqrt(metrics['mse'])
    elif model_type == 'classification':
        metrics['accuracy'] = accuracy_score(y_true, y_pred)
    else:
        raise ValueError("Invalid model type. Choose 'regression' or 'classification'.")
    
    return metrics

def save_results(results: dict, file_path: str):
    """
    Save results to a JSON file.

    Parameters:
    results (dict): Results to save.
    file_path (str): Path to the output JSON file.
    """
    with open(file_path, 'w') as file:
        json.dump(results, file, indent=4)

def normalize_data(X: np.ndarray) -> np.ndarray:
    """
    Normalize the feature data to a range of [0, 1].

    Parameters:
    X (np.ndarray): Feature data to normalize.

    Returns:
    np.ndarray: Normalized feature data.
    """
    return (X - np.min(X, axis=0)) / (np.max(X, axis=0) - np.min(X, axis=0))

# Example usage:
if __name__ == "__main__":
    # Load data
    df = load_data('data.json')
    
    # Preprocess data
    X, y = preprocess_data(df, target_column='target')
    
    # Normalize features
    X_normalized = normalize_data(X)
    
    # Split data
    X_train, X_test, y_train, y_test = split_data(X_normalized, y)
    
    # Example model evaluation (dummy predictions for demonstration)
    y_pred = np.random.choice(y_test)  # Replace with actual model predictions
    metrics = evaluate_model(y_test, y_pred, model_type='classification')
    
    # Save results
    save_results(metrics, 'evaluation_results.json')
    print("Evaluation metrics saved:", metrics)

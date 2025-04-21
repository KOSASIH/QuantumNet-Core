"""
Utility Functions for Autonomous Quantum Knowledge Distillation (AQKD)
"""
import numpy as np
from sklearn.model_selection import train_test_split

def preprocess_data(data: np.ndarray, method: str = 'standardize') -> np.ndarray:
    """
    Preprocess the input data for training and evaluation.

    Parameters:
    data (np.ndarray): Raw input data.
    method (str): Preprocessing method ('standardize', 'normalize', 'minmax').

    Returns:
    np.ndarray: Preprocessed data.
    """
    if method == 'standardize':
        # Standardization (Z-score normalization)
        return (data - np.mean(data, axis=0)) / np.std(data, axis=0)
    elif method == 'normalize':
        # Normalization (L2 normalization)
        norm = np.linalg.norm(data, axis=1, keepdims=True)
        return data / norm
    elif method == 'minmax':
        # Min-Max scaling
        return (data - np.min(data, axis=0)) / (np.max(data, axis=0) - np.min(data, axis=0))
    else:
        raise ValueError("Invalid preprocessing method. Choose 'standardize', 'normalize', or 'minmax'.")

def split_data(data: np.ndarray, labels: np.ndarray = None, train_size: float = 0.8, random_state: int = 42) -> tuple:
    """
    Split the data into training and testing sets.

    Parameters:
    data (np.ndarray): Input data to be split.
    labels (np.ndarray): Corresponding labels for the data (optional).
    train_size (float): Proportion of data to use for training.
    random_state (int): Random seed for reproducibility.

    Returns:
    tuple: Training and testing data (and labels if provided).
    """
    if labels is not None:
        return train_test_split(data, labels, train_size=train_size, random_state=random_state)
    else:
        # If no labels are provided, split the data only
        np.random.shuffle(data)
        split_index = int(len(data) * train_size)
        return data[:split_index], data[split_index:]

# Example usage:
if __name__ == "__main__":
    # Generate synthetic data
    data = np.random.rand(100, 5)  # 100 samples, 5 features
    labels = np.random.randint(0, 2, size=100)  # Binary labels

    # Preprocess data
    preprocessed_data = preprocess_data(data, method='standardize')
    print("Preprocessed Data:\n", preprocessed_data)

    # Split data
    train_data, test_data, train_labels, test_labels = split_data(preprocessed_data, labels)
    print("Training Data Shape:", train_data.shape)
    print("Testing Data Shape:", test_data.shape)

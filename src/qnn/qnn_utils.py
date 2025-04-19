# src/qnn/qnn_utils.py

import numpy as np
import matplotlib.pyplot as plt

def preprocess_data(data, method='min-max'):
    """Preprocess input data for the QNN.
    
    Args:
        data (np.ndarray): Input data to preprocess.
        method (str): Normalization method ('min-max' or 'z-score').
    
    Returns:
        np.ndarray: Normalized data.
    """
    if not isinstance(data, np.ndarray):
        raise ValueError("Input data must be a numpy array.")
    
    if method == 'min-max':
        data_min = np.min(data)
        data_max = np.max(data)
        normalized_data = (data - data_min) / (data_max - data_min)
    elif method == 'z-score':
        mean = np.mean(data)
        std = np.std(data)
        normalized_data = (data - mean) / std
    else:
        raise ValueError("Unsupported normalization method. Use 'min-max' or 'z-score'.")
    
    return normalized_data

def data_augmentation(data, factor=1.5):
    """Augment the input data by adding noise.
    
    Args:
        data (np.ndarray): Input data to augment.
        factor (float): Factor to control the amount of noise.
    
    Returns:
        np.ndarray: Augmented data.
    """
    noise = np.random.normal(0, factor, data.shape)
    augmented_data = data + noise
    return augmented_data

def postprocess_results(results, return_entropy=False):
    """Postprocess the results from the QNN.
    
    Args:
        results (np.ndarray): Array of probabilities.
        return_entropy (bool): Whether to return entropy of the results.
    
    Returns:
        dict: Processed results with probabilities and optional entropy.
    """
    if not isinstance(results, np.ndarray):
        raise ValueError("Results must be a numpy array.")
    
    probabilities = {f"State {i}": prob for i, prob in enumerate(results)}
    
    if return_entropy:
        entropy = -np.sum(results * np.log2(results + 1e-10))  # Adding a small value to avoid log(0)
        probabilities['Entropy'] = entropy
    
    return probabilities

def visualize_results(results):
    """Visualize the results of the predictions.
    
    Args:
        results (dict): Dictionary of results to visualize.
    """
    states = list(results.keys())
    probabilities = list(results.values())
    
    plt.bar(states, probabilities, color='blue')
    plt.xlabel('Quantum States')
    plt.ylabel('Probabilities')
    plt.title('Predicted Quantum State Probabilities')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

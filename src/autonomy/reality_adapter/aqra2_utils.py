### Updated `aqra2_utils.py`

"""
Utility functions for the Autonomous Quantum Reality Adapter (AQRA).
This module provides functions for data preprocessing, postprocessing,
and other utilities to enhance the simulation and analysis of quantum-generated models.
"""

import numpy as np
import pandas as pd

def preprocess_data(data: np.ndarray) -> np.ndarray:
    """
    Preprocess the input data for training or simulation.

    Args:
        data (np.ndarray): The input data to preprocess.

    Returns:
        np.ndarray: The preprocessed data.
    """
    # Normalize data to the range [0, 1]
    min_val = np.min(data)
    max_val = np.max(data)
    normalized_data = (data - min_val) / (max_val - min_val)
    return normalized_data

def postprocess_data(data: np.ndarray) -> np.ndarray:
    """
    Postprocess the generated data for analysis or visualization.

    Args:
        data (np.ndarray): The generated data to postprocess.

    Returns:
        np.ndarray: The postprocessed data.
    """
    # Scale data to a specified range, e.g., [0, 100]
    scaled_data = data * 100  # Example scaling
    return scaled_data

def save_data_to_csv(data: np.ndarray, filename: str):
    """
    Save the generated data to a CSV file for further analysis.

    Args:
        data (np.ndarray): The data to save.
        filename (str): The name of the file to save the data to.
    """
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def load_data_from_csv(filename: str) -> np.ndarray:
    """
    Load data from a CSV file.

    Args:
        filename (str): The name of the file to load data from.

    Returns:
        np.ndarray: The loaded data.
    """
    df = pd.read_csv(filename)
    return df.values

def calculate_statistics(data: np.ndarray) -> dict:
    """
    Calculate basic statistics of the data.

    Args:
        data (np.ndarray): The data to analyze.

    Returns:
        dict: A dictionary containing mean, variance, and standard deviation.
    """
    mean = np.mean(data, axis=0)
    variance = np.var(data, axis=0)
    std_dev = np.std(data, axis=0)
    return {
        'mean': mean,
        'variance': variance,
        'std_dev': std_dev
    }

def visualize_statistics(statistics: dict):
    """
    Visualize the statistics of the data.

    Args:
        statistics (dict): A dictionary containing statistics to visualize.
    """
    import matplotlib.pyplot as plt

    # Plot mean, variance, and standard deviation
    labels = list(statistics.keys())
    values = [statistics[label] for label in labels]

    x = np.arange(len(labels))  # the label locations
    width = 0.2  # the width of the bars

    fig, ax = plt.subplots()
    bars = ax.bar(x - width, values[0], width, label='Mean')
    bars = ax.bar(x, values[1], width, label='Variance')
    bars = ax.bar(x + width, values[2], width, label='Std Dev')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Values')
    ax.set_title('Statistics of Generated Data')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    plt.show()

# Example usage
if __name__ == "__main__":
    # Generate some random data for demonstration
    sample_data = np.random.rand(100, 4)  # 100 samples, 4 features

    # Preprocess the data
    preprocessed_data = preprocess_data(sample_data)

    # Save the preprocessed data to CSV
    save_data_to_csv(preprocessed_data, 'preprocessed_data.csv')

    # Load the data back from CSV
    loaded_data = load_data_from_csv('preprocessed_data.csv')

    # Calculate statistics
    stats = calculate_statistics(loaded_data)

    # Visualize statistics
    visualize_statistics(stats)

"""
Utility Functions for Quantum Consciousness Emulator (QCE).
"""
import numpy as np

def generate_crisis_data(n_features: int, scale: float = 1.0) -> np.ndarray:
    """
    Generate random crisis data for testing.

    Parameters:
    n_features (int): Number of features in the crisis data.
    scale (float): Scale factor to adjust the range of generated data.

    Returns:
    np.ndarray: Randomly generated crisis data.
    """
    return np.random.rand(n_features) * scale  # Scale the random data

def analyze_state(state: np.ndarray) -> dict:
    """
    Analyze the state of the consciousness model.

    Parameters:
    state (np.ndarray): Current state of the consciousness model.

    Returns:
    dict: Analysis results including mean, variance, max, and min.
    """
    return {
        'mean': np.mean(state),
        'variance': np.var(state),
        'max': np.max(state),
        'min': np.min(state),
        'std_dev': np.std(state),  # Added standard deviation
        'median': np.median(state)  # Added median
    }

def normalize_state(state: np.ndarray) -> np.ndarray:
    """
    Normalize the state of the consciousness model to a range of [0, 1].

    Parameters:
    state (np.ndarray): Current state of the consciousness model.

    Returns:
    np.ndarray: Normalized state.
    """
    min_val = np.min(state)
    max_val = np.max(state)
    if max_val - min_val == 0:
        return np.zeros_like(state)  # Avoid division by zero
    return (state - min_val) / (max_val - min_val)

def generate_crisis_scenarios(n_scenarios: int, n_features: int, scale: float = 1.0) -> list:
    """
    Generate a list of random crisis scenarios.

    Parameters:
    n_scenarios (int): Number of crisis scenarios to generate.
    n_features (int): Number of features in each crisis scenario.
    scale (float): Scale factor to adjust the range of generated data.

    Returns:
    list: List of randomly generated crisis scenarios.
    """
    return [generate_crisis_data(n_features, scale) for _ in range(n_scenarios)]

# Example usage:
if __name__ == "__main__":
    # Generate random crisis data
    crisis_data = generate_crisis_data(5, scale=10)
    print("Crisis Data:", crisis_data)

    # Analyze the state
    analysis = analyze_state(crisis_data)
    print("State Analysis:", analysis)

    # Normalize the state
    normalized_state = normalize_state(crisis_data)
    print("Normalized State:", normalized_state)

    # Generate multiple crisis scenarios
    scenarios = generate_crisis_scenarios(3, 5, scale=10)
    print("Crisis Scenarios:", scenarios)

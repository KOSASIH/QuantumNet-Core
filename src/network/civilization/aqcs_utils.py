"""
Utilities for Autonomous Quantum Civilization Synthesizer (AQCS).
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_average_state(agent_states: np.ndarray) -> float:
    """
    Calculate the average state of agents.

    Args:
        agent_states (np.ndarray): Array of agent states.

    Returns:
        float: Average state of the agents.
    """
    return np.mean(agent_states)

def normalize_states(agent_states: np.ndarray) -> np.ndarray:
    """
    Normalize agent states to the range [0, 1].

    Args:
        agent_states (np.ndarray): Array of agent states.

    Returns:
        np.ndarray: Normalized agent states.
    """
    min_state = np.min(agent_states)
    max_state = np.max(agent_states)
    if max_state == min_state:
        return np.zeros_like(agent_states)  # Avoid division by zero
    return (agent_states - min_state) / (max_state - min_state)

def plot_agent_states(agent_states: np.ndarray, title: str = "Agent States Over Time"):
    """
    Plot the states of agents over time.

    Args:
        agent_states (np.ndarray): Array of agent states.
        title (str): Title of the plot.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(agent_states, marker='o', linestyle='-', alpha=0.7)
    plt.title(title)
    plt.xlabel("Agent Index")
    plt.ylabel("State Value")
    plt.ylim(0, 1)
    plt.grid()
    plt.show()

def calculate_entropy(agent_states: np.ndarray) -> float:
    """
    Calculate the Shannon entropy of the agent states.

    Args:
        agent_states (np.ndarray): Array of agent states.

    Returns:
        float: Shannon entropy.
    """
    value_counts = np.bincount(agent_states.astype(int))
    probabilities = value_counts / len(agent_states)
    probabilities = probabilities[probabilities > 0]  # Remove zero probabilities
    return -np.sum(probabilities * np.log(probabilities))

def visualize_civilization_distribution(agent_states: np.ndarray, title: str = "Civilization State Distribution"):
    """
    Visualize the distribution of agent states in the civilization.

    Args:
        agent_states (np.ndarray): Array of agent states.
        title (str): Title of the plot.
    """
    plt.figure(figsize=(12, 6))
    sns.histplot(agent_states, bins=20, kde=True)
    plt.title(title)
    plt.xlabel("State Value")
    plt.ylabel("Frequency")
    plt.grid()
    plt.show()

def save_agent_states(agent_states: np.ndarray, filename: str):
    """
    Save the agent states to a file.

    Args:
        agent_states (np.ndarray): Array of agent states.
        filename (str): Filename to save the states.
    """
    np.save(filename, agent_states)
    print(f"Agent states saved to {filename}")

def load_agent_states(filename: str) -> np.ndarray:
    """
    Load agent states from a file.

    Args:
        filename (str): Filename to load the states from.

    Returns:
        np.ndarray: Loaded agent states.
    """
    agent_states = np.load(filename)
    print(f"Agent states loaded from {filename}")
    return agent_states

# Example usage
if __name__ == "__main__":
    # Generate synthetic agent states for testing
    agent_states = np.random.rand(100)

    # Normalize states
    normalized_states = normalize_states(agent_states)
    print("Normalized States:", normalized_states)

    # Calculate average state
    average_state = calculate_average_state(agent_states)
    print("Average State:", average_state)

    # Calculate entropy
    entropy = calculate_entropy(agent_states)
    print("Shannon Entropy:", entropy)

    # Visualize agent states
    plot_agent_states(normalized_states)

    # Visualize civilization distribution
    visualize_civilization_distribution(agent_states)

    # Save and load agent states
    save_agent_states(agent_states, "agent_states.npy")
    loaded_states = load_agent_states("agent_states.npy")

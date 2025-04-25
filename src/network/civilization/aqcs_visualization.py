"""
Visualization tools for Autonomous Quantum Civilization Synthesizer (AQCS).
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

def plot_2d_agent_states(agent_states: np.ndarray, title: str = "2D Agent States Visualization"):
    """
    Plot the states of agents in a 2D space.

    Args:
        agent_states (np.ndarray): Array of agent states.
        title (str): Title of the plot.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(range(len(agent_states)), agent_states, c=agent_states, cmap='viridis', alpha=0.7)
    plt.colorbar(label='State Value')
    plt.title(title)
    plt.xlabel("Agent Index")
    plt.ylabel("State Value")
    plt.grid()
    plt.show()

def plot_3d_agent_states(agent_states: np.ndarray, title: str = "3D Agent States Visualization"):
    """
    Plot the states of agents in a 3D space.

    Args:
        agent_states (np.ndarray): Array of agent states.
        title (str): Title of the plot.
    """
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(range(len(agent_states)), agent_states, zs=0, zdir='y', c=agent_states, cmap='plasma', alpha=0.7)
    ax.set_title(title)
    ax.set_xlabel("Agent Index")
    ax.set_ylabel("State Value")
    ax.set_zlabel("Z-axis (Static)")
    plt.show()

def visualize_state_distribution(agent_states: np.ndarray, title: str = "State Distribution"):
    """
    Visualize the distribution of agent states using a histogram.

    Args:
        agent_states (np.ndarray): Array of agent states.
        title (str): Title of the plot.
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(agent_states, bins=30, kde=True, color='blue')
    plt.title(title)
    plt.xlabel("State Value")
    plt.ylabel("Frequency")
    plt.grid()
    plt.show()

def create_heatmap(agent_states: np.ndarray, title: str = "Agent States Heatmap"):
    """
    Create a heatmap of agent states.

    Args:
        agent_states (np.ndarray): 2D array of agent states.
        title (str): Title of the heatmap.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(agent_states, cmap='coolwarm', annot=True, fmt=".2f")
    plt.title(title)
    plt.xlabel("Agent Index")
    plt.ylabel("State Value")
    plt.show()

# Example usage
if __name__ == "__main__":
    # Generate synthetic agent states for testing
    agent_states = np.random.rand(100)

    # 2D Visualization
    plot_2d_agent_states(agent_states)

    # 3D Visualization
    plot_3d_agent_states(agent_states)

    # State Distribution Visualization
    visualize_state_distribution(agent_states)

    # Create a heatmap (for demonstration, reshaping for 2D)
    agent_states_2d = agent_states.reshape(10, 10)  # Example reshaping
    create_heatmap(agent_states_2d)

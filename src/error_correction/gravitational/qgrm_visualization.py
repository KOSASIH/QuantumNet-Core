"""
Visualization Tools for the Quantum Gravitational Resilience Module (QGRM)
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

def plot_gravitational_field(gravity_field: np.ndarray, title: str = "Gravitational Field"):
    """
    Plot the gravitational field strengths.

    Parameters:
    gravity_field (np.ndarray): Array representing the gravitational field strengths.
    title (str): Title of the plot.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(gravity_field)), gravity_field, color='blue', alpha=0.7)
    plt.title(title)
    plt.xlabel("Qubit Index")
    plt.ylabel("Gravitational Field Strength")
    plt.grid()
    plt.show()

def plot_quantum_state_distribution(counts: dict, title: str = "Quantum State Distribution"):
    """
    Plot the distribution of quantum states from measurement results.

    Parameters:
    counts (dict): Measurement results as a dictionary of state counts.
    title (str): Title of the plot.
    """
    plt.figure(figsize=(10, 6))
    states = list(counts.keys())
    values = list(counts.values())
    plt.bar(states, values, color='green', alpha=0.7)
    plt.title(title)
    plt.xlabel("Quantum States")
    plt.ylabel("Counts")
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

def plot_heatmap(data: np.ndarray, title: str = "Heatmap of Gravitational Effects"):
    """
    Plot a heatmap to visualize the effects of gravity on quantum systems.

    Parameters:
    data (np.ndarray): 2D array representing the effects of gravity.
    title (str): Title of the plot.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(data, cmap='viridis', annot=True, fmt=".2f")
    plt.title(title)
    plt.xlabel("Qubit Index")
    plt.ylabel("Time Steps")
    plt.colorbar(label="Effect Magnitude")
    plt.show()

def plot_3d_gravitational_effects(gravity_field: np.ndarray, time_steps: int, title: str = "3D Gravitational Effects"):
    """
    Plot a 3D surface plot to visualize gravitational effects over time.

    Parameters:
    gravity_field (np.ndarray): Array representing the gravitational field strengths.
    time_steps (int): Number of time steps to simulate.
    title (str): Title of the plot.
    """
    x = np.arange(len(gravity_field))
    y = np.linspace(0, time_steps, time_steps)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X) * np.cos(Y)  # Example function to simulate gravitational effects

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='plasma', edgecolor='none')
    ax.set_title(title)
    ax.set_xlabel("Qubit Index")
    ax.set_ylabel("Time Steps")
    ax.set_zlabel("Gravitational Effect Magnitude")
    plt.show()

# Example usage:
if __name__ == "__main__":
    # Example gravitational field data
    gravity_field = np.random.uniform(-1, 1, size=5)
    plot_gravitational_field(gravity_field)

    # Example quantum state distribution
    counts = {'000': 300, '001': 150, '010': 200, '011': 100, '100': 250}
    plot_quantum_state_distribution(counts)

    # Example heatmap data
    heatmap_data = np.random.rand(5, 10)  # 5 qubits, 10 time steps
    plot_heatmap(heatmap_data)

    # Example 3D plot
    plot_3d_gravitational_effects(gravity_field, time_steps=10)

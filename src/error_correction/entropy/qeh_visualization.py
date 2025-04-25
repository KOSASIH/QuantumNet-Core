"""
Visualization module for Quantum Entropy Harmonizer (QEH).
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation

class QEHVisualization:
    @staticmethod
    def plot_entropy_distribution(entropy_values: np.ndarray):
        """
        Plot the distribution of entropy values as a histogram.

        Args:
            entropy_values (np.ndarray): Array of entropy values.
        """
        plt.figure(figsize=(10, 6))
        plt.hist(entropy_values, bins=30, alpha=0.7, color='blue')
        plt.title('Entropy Distribution')
        plt.xlabel('Entropy Values')
        plt.ylabel('Frequency')
        plt.grid()
        plt.show()

    @staticmethod
    def plot_density_matrix(density_matrix: np.ndarray):
        """
        Plot the density matrix as a heatmap.

        Args:
            density_matrix (np.ndarray): Density matrix of the quantum state.
        """
        plt.figure(figsize=(8, 6))
        sns.heatmap(density_matrix, annot=True, cmap='viridis', square=True)
        plt.title('Density Matrix Heatmap')
        plt.xlabel('Basis States')
        plt.ylabel('Basis States')
        plt.show()

    @staticmethod
    def animate_quantum_state_evolution(states: list):
        """
        Animate the evolution of quantum states over time.

        Args:
            states (list): List of density matrices representing quantum states over time.
        """
        fig, ax = plt.subplots(figsize=(8, 6))
        heatmap = sns.heatmap(states[0], annot=True, cmap='viridis', square=True, cbar=False)

        def update(frame):
            ax.clear()
            sns.heatmap(states[frame], annot=True, cmap='viridis', square=True, cbar=False, ax=ax)
            ax.set_title(f'Quantum State Evolution: Frame {frame + 1}')

        ani = FuncAnimation(fig, update, frames=len(states), repeat=True)
        plt.show()

# Example usage
if __name__ == "__main__":
    # Example usage of QEHVisualization
    entropy_values = np.random.rand(100)  # Example entropy values
    QEHVisualization.plot_entropy_distribution(entropy_values)

    density_matrix = np.random.rand(4, 4)  # Example density matrix
    QEHVisualization.plot_density_matrix(density_matrix)

    states = [np.random.rand(4, 4) for _ in range(10)]  # Example list of density matrices
    QEHVisualization.animate_quantum_state_evolution(states)

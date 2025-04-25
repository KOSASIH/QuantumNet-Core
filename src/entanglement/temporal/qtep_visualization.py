"""
Visualization Utilities for Quantum Temporal Entanglement Processor (QTEP).
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class QTEPVisualization:
    @staticmethod
    def plot_probability_distribution(state: np.ndarray, title: str = "Quantum State Probability Distribution"):
        """
        Plot the probability distribution of a quantum state.

        Args:
            state (np.ndarray): The quantum state to visualize.
            title (str): The title of the plot.
        """
        probabilities = np.abs(state)**2
        plt.figure(figsize=(10, 6))
        plt.bar(range(len(state)), probabilities, color='blue', alpha=0.7)
        plt.title(title)
        plt.xlabel("Basis States")
        plt.ylabel("Probability Amplitude")
        plt.xticks(range(len(state)))
        plt.grid()
        plt.show()

    @staticmethod
    def plot_state_evolution(states: np.ndarray, title: str = "Quantum State Evolution Over Time"):
        """
        Visualize the evolution of quantum states over time.

        Args:
            states (np.ndarray): An array of quantum states at each time step.
            title (str): The title of the plot.
        """
        time_steps = states.shape[0]
        plt.figure(figsize=(12, 8))
        for i in range(states.shape[1]):
            plt.plot(range(time_steps), np.abs(states[:, i])**2, label=f'Qubit {i+1}')
        
        plt.title(title)
        plt.xlabel("Time Steps")
        plt.ylabel("Probability Amplitude")
        plt.legend()
        plt.grid()
        plt.show()

    @staticmethod
    def plot_density_matrix(density_matrix: np.ndarray, title: str = "Density Matrix"):
        """
        Visualize the density matrix of a quantum state.

        Args:
            density_matrix (np.ndarray): The density matrix to visualize.
            title (str): The title of the plot.
        """
        plt.figure(figsize=(8, 6))
        sns.heatmap(np.abs(density_matrix), annot=True, fmt=".2f", cmap='viridis', square=True)
        plt.title(title)
        plt.xlabel("Basis States")
        plt.ylabel("Basis States")
        plt.colorbar(label='Magnitude')
        plt.show()

    @staticmethod
    def plot_measurement_results(results: list, title: str = "Measurement Results"):
        """
        Visualize the results of multiple measurements.

        Args:
            results (list): A list of measurement results.
            title (str): The title of the plot.
        """
        plt.figure(figsize=(10, 6))
        sns.histplot(results, bins=np.arange(min(results), max(results) + 1, 1), kde=False, color='blue', alpha=0.7)
        plt.title(title)
        plt.xlabel("Measurement Outcome")
        plt.ylabel("Frequency")
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Example quantum state
    num_qubits = 3
    initial_state = np.random.rand(2**num_qubits) + 1j * np.random.rand(2**num_qubits)
    initial_state /= np.linalg.norm(initial_state)  # Normalize the state

    # Visualize the probability distribution
    QTEPVisualization.plot_probability_distribution(initial_state)

    # Simulate state evolution (for demonstration)
    states = np.array([initial_state * (0.9 ** t) for t in range(10)])  # Example decay over time
    QTEPVisualization.plot_state_evolution(states)

    # Example density matrix
    density_matrix = np.outer(initial_state, initial_state.conj())
    QTEPVisualization.plot_density_matrix(density_matrix)

    # Example measurement results
    measurement_results = [np.random.choice([0, 1], p=[0.5, 0.5]) for _ in range(100)]
    QTEPVisualization.plot_measurement_results(measurement_results)

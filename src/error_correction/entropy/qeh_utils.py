"""
Utilities for Quantum Entropy Harmonizer (QEH).
"""
import numpy as np
from qiskit.quantum_info import DensityMatrix

class QEHUtils:
    @staticmethod
    def normalize_entropy(entropy_values: np.ndarray) -> np.ndarray:
        """
        Normalize entropy values to the range [0, 1].

        Args:
            entropy_values (np.ndarray): Array of entropy values.

        Returns:
            np.ndarray: Normalized entropy values.
        """
        min_entropy = np.min(entropy_values)
        max_entropy = np.max(entropy_values)
        if max_entropy == min_entropy:
            return np.zeros_like(entropy_values)  # Avoid division by zero
        return (entropy_values - min_entropy) / (max_entropy - min_entropy)

    @staticmethod
    def calculate_average_entropy(entropy_values: np.ndarray) -> float:
        """
        Calculate the average entropy.

        Args:
            entropy_values (np.ndarray): Array of entropy values.

        Returns:
            float: Average entropy.
        """
        return np.mean(entropy_values)

    @staticmethod
    def generate_random_density_matrix(n_qubits: int) -> np.ndarray:
        """
        Generate a random density matrix for a quantum state.

        Args:
            n_qubits (int): Number of qubits.

        Returns:
            np.ndarray: Random density matrix of shape (2^n_qubits, 2^n_qubits).
        """
        dim = 2 ** n_qubits
        random_state = np.random.rand(dim) + 1j * np.random.rand(dim)  # Random complex vector
        random_state /= np.linalg.norm(random_state)  # Normalize to unit length
        density_matrix = np.outer(random_state, random_state.conj())  # Create density matrix
        return density_matrix

    @staticmethod
    def calculate_entropy_of_density_matrix(density_matrix: np.ndarray) -> float:
        """
        Calculate the Von Neumann entropy of a density matrix.

        Args:
            density_matrix (np.ndarray): Density matrix of the quantum state.

        Returns:
            float: Von Neumann entropy.
        """
        dm = DensityMatrix(density_matrix)
        return dm.entropy()

# Example usage
if __name__ == "__main__":
    # Example usage of QEHUtils
    n_qubits = 2
    random_density_matrix = QEHUtils.generate_random_density_matrix(n_qubits)
    print("Random Density Matrix:\n", random_density_matrix)

    entropy = QEHUtils.calculate_entropy_of_density_matrix(random_density_matrix)
    print("Von Neumann Entropy:", entropy)

    entropy_values = np.array([0.5, 1.0, 1.5, 2.0])
    normalized_entropy = QEHUtils.normalize_entropy(entropy_values)
    print("Normalized Entropy Values:", normalized_entropy)

    average_entropy = QEHUtils.calculate_average_entropy(entropy_values)
    print("Average Entropy:", average_entropy)

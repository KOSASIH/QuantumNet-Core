"""
Utilities for Quantum Temporal Entanglement Processor (QTEP).
"""
import numpy as np
import pennylane as qml

class QTEPUtils:
    @staticmethod
    def prepare_initial_state(num_qubits: int, state_type: str = 'random') -> np.ndarray:
        """
        Prepare the initial quantum state.

        Args:
            num_qubits (int): The number of qubits.
            state_type (str): The type of state to prepare ('random', 'zero', 'one', 'superposition').

        Returns:
            np.ndarray: The prepared initial quantum state.
        """
        if state_type == 'random':
            return np.random.randint(0, 2, num_qubits)
        elif state_type == 'zero':
            return np.zeros(num_qubits)
        elif state_type == 'one':
            return np.ones(num_qubits)
        elif state_type == 'superposition':
            state = np.zeros(2**num_qubits)
            state[0] = 1 / np.sqrt(2)  # |0> state
            state[1] = 1 / np.sqrt(2)  # |1> state
            return state
        else:
            raise ValueError("Invalid state type. Choose from 'random', 'zero', 'one', 'superposition'.")

    @staticmethod
    def apply_noise(state: np.ndarray, noise_level: float) -> np.ndarray:
        """
        Apply noise to the quantum state.

        Args:
            state (np.ndarray): The quantum state to which noise will be applied.
            noise_level (float): The level of noise to apply (0 to 1).

        Returns:
            np.ndarray: The noisy quantum state.
        """
        if not (0 <= noise_level <= 1):
            raise ValueError("Noise level must be between 0 and 1.")

        noise = np.random.rand(*state.shape) < noise_level
        noisy_state = np.where(noise, np.random.randint(0, 2, state.shape), state)
        return noisy_state

    @staticmethod
    def measure_state(state: np.ndarray) -> int:
        """
        Measure the quantum state.

        Args:
            state (np.ndarray): The quantum state to measure.

        Returns:
            int: The measurement result (0 or 1).
        """
        probabilities = np.abs(state)**2
        return np.random.choice(len(state), p=probabilities)

    @staticmethod
    def convert_to_density_matrix(state: np.ndarray) -> np.ndarray:
        """
        Convert a quantum state to its density matrix representation.

        Args:
            state (np.ndarray): The quantum state.

        Returns:
            np.ndarray: The density matrix of the quantum state.
        """
        return np.outer(state, state.conj())

    @staticmethod
    def visualize_state(state: np.ndarray):
        """
        Visualize the quantum state.

        Args:
            state (np.ndarray): The quantum state to visualize.
        """
        import matplotlib.pyplot as plt

        plt.figure(figsize=(10, 6))
        plt.bar(range(len(state)), np.abs(state)**2, color='blue', alpha=0.7)
        plt.title("Quantum State Probability Distribution")
        plt.xlabel("Basis States")
        plt.ylabel("Probability Amplitude")
        plt.xticks(range(len(state)))
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    num_qubits = 3
    initial_state = QTEPUtils.prepare_initial_state(num_qubits, 'superposition')
    print("Initial State:", initial_state)

    noisy_state = QTEPUtils.apply_noise(initial_state, 0.1)
    print("Noisy State:", noisy_state)

    measurement = QTEPUtils.measure_state(noisy_state)
    print("Measurement Result:", measurement)

    density_matrix = QTEPUtils.convert_to_density_matrix(noisy_state)
    print("Density Matrix:\n", density_matrix)

    QTEPUtils.visualize_state(noisy_state)

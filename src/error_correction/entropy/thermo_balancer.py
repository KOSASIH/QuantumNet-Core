"""
Quantum Thermodynamic Balancer.
"""
import numpy as np

class ThermoBalancer:
    def __init__(self, n_qubits: int):
        """
        Initialize the Thermo Balancer.

        Args:
            n_qubits (int): The number of qubits in the quantum system.
        """
        self.n_qubits = n_qubits

    def calculate_partition_function(self, energy_levels: np.ndarray, temperature: float) -> float:
        """
        Calculate the partition function for the quantum system.

        Args:
            energy_levels (np.ndarray): Energy levels of the quantum system.
            temperature (float): Temperature of the system.

        Returns:
            float: Partition function.
        """
        if temperature <= 0:
            raise ValueError("Temperature must be positive.")
        
        partition_function = np.sum(np.exp(-energy_levels / temperature))
        return partition_function

    def balance_system(self, energy_levels: np.ndarray, temperature: float) -> np.ndarray:
        """
        Balance the quantum system thermodynamically.

        Args:
            energy_levels (np.ndarray): Energy levels of the quantum system.
            temperature (float): Temperature of the system.

        Returns:
            np.ndarray: Balanced state probabilities.
        """
        partition_function = self.calculate_partition_function(energy_levels, temperature)
        probabilities = np.exp(-energy_levels / temperature) / partition_function  # Boltzmann distribution
        return probabilities

    def adjust_state_probabilities(self, probabilities: np.ndarray) -> np.ndarray:
        """
        Adjust state probabilities to ensure they sum to 1.

        Args:
            probabilities (np.ndarray): Array of state probabilities.

        Returns:
            np.ndarray: Normalized state probabilities.
        """
        total_probability = np.sum(probabilities)
        if total_probability == 0:
            raise ValueError("Total probability cannot be zero.")
        return probabilities / total_probability

# Example usage
if __name__ == "__main__":
    n_qubits = 2
    balancer = ThermoBalancer(n_qubits)

    # Example energy levels for testing
    energy_levels = np.array([0.0, 1.0, 2.0])  # Energy levels in arbitrary units
    temperature = 1.0  # Temperature in arbitrary units

    # Balance the quantum system
    balanced_probabilities = balancer.balance_system(energy_levels, temperature)
    print("Balanced State Probabilities:", balanced_probabilities)

    # Adjust state probabilities
    adjusted_probabilities = balancer.adjust_state_probabilities(balanced_probabilities)
    print("Adjusted State Probabilities:", adjusted_probabilities)

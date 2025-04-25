"""
Entropy Simulator for Quantum Fluctuations.
"""
import numpy as np
import matplotlib.pyplot as plt

class EntropySimulator:
    def __init__(self, num_steps: int, initial_entropy: float, fluctuation_strength: float = 0.1):
        """
        Initialize the Entropy Simulator.

        Args:
            num_steps (int): Number of simulation steps.
            initial_entropy (float): Initial entropy of the system.
            fluctuation_strength (float): Strength of random fluctuations.
        """
        self.num_steps = num_steps
        self.initial_entropy = initial_entropy
        self.fluctuation_strength = fluctuation_strength
        self.entropy_values = [initial_entropy]

    def simulate_fluctuations(self):
        """Simulate entropy fluctuations over time."""
        for _ in range(1, self.num_steps):
            fluctuation = np.random.normal(0, self.fluctuation_strength)  # Random fluctuation
            new_entropy = self.entropy_values[-1] + fluctuation
            self.entropy_values.append(max(new_entropy, 0))  # Ensure non-negative entropy

        return np.array(self.entropy_values)

    def visualize_entropy(self):
        """Visualize the entropy fluctuations over time."""
        plt.figure(figsize=(10, 6))
        plt.plot(self.entropy_values, marker='o', linestyle='-', color='blue', alpha=0.7)
        plt.title("Entropy Fluctuations Over Time")
        plt.xlabel("Time Step")
        plt.ylabel("Entropy Value")
        plt.grid()
        plt.axhline(y=self.initial_entropy, color='r', linestyle='--', label='Initial Entropy')
        plt.legend()
        plt.show()

# Example usage
if __name__ == "__main__":
    num_steps = 100
    initial_entropy = 1.0
    fluctuation_strength = 0.1

    simulator = EntropySimulator(num_steps, initial_entropy, fluctuation_strength)

    # Simulate entropy fluctuations
    entropy_values = simulator.simulate_fluctuations()

    # Visualize the results
    simulator.visualize_entropy()

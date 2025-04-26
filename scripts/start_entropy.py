"""
Script for Launching Quantum Entropy Harmonizer (QEH).
"""
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import Statevector, entropy

class QuantumEntropyHarmonizer:
    def __init__(self, n_qubits: int):
        """
        Initialize the Quantum Entropy Harmonizer.

        Args:
            n_qubits (int): Number of qubits for the harmonizer.
        """
        self.n_qubits = n_qubits
        self.backend = Aer.get_backend('statevector_simulator')

    def create_random_state(self) -> Statevector:
        """Create a random quantum state."""
        circuit = QuantumCircuit(self.n_qubits)
        for qubit in range(self.n_qubits):
            circuit.h(qubit)  # Apply Hadamard gate to create superposition
        return self.simulate_circuit(circuit)

    def simulate_circuit(self, circuit: QuantumCircuit) -> Statevector:
        """Simulate the quantum circuit and return the resulting state."""
        result = execute(circuit, self.backend).result()
        return result.get_statevector()

    def calculate_entropy(self, state: Statevector) -> float:
        """Calculate the von Neumann entropy of a quantum state."""
        density_matrix = state.to_density_matrix()
        return entropy(density_matrix)

    def harmonize_entropy(self, state: Statevector) -> Statevector:
        """Harmonize the entropy of a quantum state."""
        current_entropy = self.calculate_entropy(state)
        target_entropy = 0.5  # Target entropy for harmonization (example)
        
        if current_entropy < target_entropy:
            # Apply a Hadamard gate to increase entropy
            circuit = QuantumCircuit(self.n_qubits)
            for qubit in range(self.n_qubits):
                circuit.h(qubit)
            return self.simulate_circuit(circuit)
        return state  # Return the original state if already harmonized

    def visualize_state(self, state: Statevector):
        """Visualize the quantum state as a bar chart."""
        probabilities = np.abs(state)**2
        plt.bar(range(len(probabilities)), probabilities)
        plt.xlabel('Basis States')
        plt.ylabel('Probabilities')
        plt.title('Quantum State Probability Distribution')
        plt.xticks(range(len(probabilities)), [f'|{i:0{self.n_qubits}b}>' for i in range(len(probabilities))])
        plt.show()

def main():
    # Initialize the Quantum Entropy Harmonizer
    n_qubits = 3  # Example: 3 qubits
    qeh = QuantumEntropyHarmonizer(n_qubits)

    # Create a random quantum state
    state = qeh.create_random_state()
    print("Created Random Quantum State:")
    print(state)

    # Calculate the entropy of the state
    entropy_value = qeh.calculate_entropy(state)
    print(f"Entropy of the State: {entropy_value:.4f}")

    # Harmonize the entropy of the state
    harmonized_state = qeh.harmonize_entropy(state)
    print("Harmonized Quantum State:")
    print(harmonized_state)

    # Visualize the original and harmonized states
    print("Visualizing Original State:")
    qeh.visualize_state(state)
    
    print("Visualizing Harmonized State:")
    qeh.visualize_state(harmonized_state)

if __name__ == "__main__":
    main()

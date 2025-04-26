"""
Script for Launching Autonomous Quantum Dimensional Navigator (AQDN).
"""
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import Statevector

class AutonomousQuantumDimensionalNavigator:
    def __init__(self, n_qubits: int):
        """
        Initialize the Autonomous Quantum Dimensional Navigator.

        Args:
            n_qubits (int): Number of qubits for the navigator.
        """
        self.n_qubits = n_qubits
        self.backend = Aer.get_backend('statevector_simulator')

    def navigate_to_dimension(self, dimension: int) -> Statevector:
        """Navigate to a specified quantum dimension."""
        if dimension < 0 or dimension >= 2**self.n_qubits:
            raise ValueError("Dimension out of bounds.")
        
        circuit = QuantumCircuit(self.n_qubits)
        # Create a superposition state to represent navigation
        for qubit in range(self.n_qubits):
            circuit.h(qubit)  # Apply Hadamard gate to create superposition
        
        return self.simulate_circuit(circuit)

    def simulate_circuit(self, circuit: QuantumCircuit) -> Statevector:
        """Simulate the quantum circuit and return the resulting state."""
        result = execute(circuit, self.backend).result()
        return result.get_statevector()

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
    # Initialize the Autonomous Quantum Dimensional Navigator
    n_qubits = 3  # Example: 3 qubits for 8 dimensions
    aqdn = AutonomousQuantumDimensionalNavigator(n_qubits)

    # Specify the dimension to navigate to
    dimension = 2  # Example dimension to navigate to
    print(f"Navigating to dimension: {dimension}")

    try:
        # Navigate to the specified dimension
        state = aqdn.navigate_to_dimension(dimension)
        print("Navigated to Quantum State:")
        print(state)

        # Visualize the quantum state
        aqdn.visualize_state(state)

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

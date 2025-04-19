from qiskit import QuantumCircuit, Aer, transpile, execute
import numpy as np
import matplotlib.pyplot as plt

class QAOAAllocator:
    def __init__(self, num_resources, cost_function):
        self.num_resources = num_resources
        self.cost_function = cost_function  # Function to minimize

    def allocate_resources(self, p):
        """Allocate resources using QAOA."""
        circuit = self.create_qaoa_circuit(p)
        result = self.run_circuit(circuit)
        return self.process_results(result)

    def create_qaoa_circuit(self, p):
        """Create a QAOA circuit."""
        circuit = QuantumCircuit(self.num_resources)
        # Add QAOA layers (cost and mixing operators)
        for layer in range(p):
            self.add_cost_layer(circuit, layer)
            self.add_mixing_layer(circuit)
        return circuit

    def add_cost_layer(self, circuit, layer):
        """Add cost layer to the QAOA circuit."""
        # Example: Implementing a simple cost function for demonstration
        for i in range(self.num_resources):
            for j in range(i + 1, self.num_resources):
                # Apply a controlled-Z gate based on the cost function
                if self.cost_function(i, j):
                    circuit.cz(i, j)

    def add_mixing_layer(self, circuit):
        """Add mixing layer to the QAOA circuit."""
        for qubit in range(self.num_resources):
            circuit.rx(np.pi / 2, qubit)

    def run_circuit(self, circuit):
        """Run the QAOA circuit on a quantum simulator."""
        backend = Aer.get_backend('aer_simulator')
        transpiled_circuit = transpile(circuit, backend)
        try:
            result = execute(transpiled_circuit, backend).result()
            return result
        except Exception as e:
            print(f"Error during circuit execution: {e}")
            return None

    def process_results(self, result):
        """Process the results of the QAOA execution."""
        counts = result.get_counts()
        # Find the optimal allocation (the one with the highest count)
        optimal_allocation = max(counts, key=counts.get)
        return optimal_allocation, counts

    def visualize_results(self, counts):
        """Visualize the results of the QAOA execution."""
        labels = counts.keys()
        values = counts.values()

        plt.figure(figsize=(10, 6))
        plt.bar(labels, values, color='blue', alpha=0.7)
        plt.title("QAOA Results")
        plt.xlabel("Resource Allocation States")
        plt.ylabel("Counts")
        plt.xticks(rotation=45)
        plt.grid(axis='y', alpha=0.75)
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    # Define a simple cost function for demonstration
    def cost_function(i, j):
        return (i + j) % 2 == 0  # Example condition

    allocator = QAOAAllocator(num_resources=3, cost_function=cost_function)
    p = 2  # Number of layers
    optimal_allocation, counts = allocator.allocate_resources(p)
    print(f"Optimal Allocation: {optimal_allocation}")
    allocator.visualize_results(counts)

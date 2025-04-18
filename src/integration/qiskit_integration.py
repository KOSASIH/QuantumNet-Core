# integration/qiskit_integration.py

from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

class QiskitIntegration:
    """Class for integrating with Qiskit for hybrid quantum-classical computing."""
    
    def __init__(self):
        """Initializes the Qiskit integration."""
        self.backend = Aer.get_backend('qasm_simulator')

    def create_circuit(self, num_qubits):
        """Creates a simple quantum circuit with the specified number of qubits.
        
        Args:
            num_qubits (int): The number of qubits in the circuit.
        
        Returns:
            QuantumCircuit: The created quantum circuit.
        """
        circuit = QuantumCircuit(num_qubits)
        circuit.h(range(num_qubits))  # Apply Hadamard gates to all qubits
        circuit.measure_all()  # Measure all qubits
        return circuit

    def run_circuit(self, circuit):
        """Runs the quantum circuit on the Qiskit simulator.
        
        Args:
            circuit (QuantumCircuit): The quantum circuit to run.
        
        Returns:
            dict: The result of the circuit execution as a histogram.
        """
        job = execute(circuit, self.backend, shots=1024)
        result = job.result()
        counts = result.get_counts(circuit)
        return counts

    def visualize_results(self, counts):
        """Visualizes the results of the quantum circuit execution.
        
        Args:
            counts (dict): The counts of measurement results.
        """
        plot_histogram(counts).show()

# Example usage
if __name__ == "__main__":
    qiskit_integration = QiskitIntegration()
    circuit = qiskit_integration.create_circuit(2)
    counts = qiskit_integration.run_circuit(circuit)
    print("Measurement results:", counts)
    qiskit_integration.visualize_results(counts)

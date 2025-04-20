"""
Circuit Evaluator for Quantum Circuits
"""
import time
from qiskit import Aer, transpile, execute
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector, Operator, fidelity

class CircuitEvaluator:
    def __init__(self, backend_name='aer_simulator'):
        """
        Initialize the Circuit Evaluator.

        Parameters:
        backend_name (str): The name of the backend to use for execution.
        """
        self.backend = Aer.get_backend(backend_name)

    def calculate_fidelity(self, circuit1, circuit2):
        """
        Calculate the fidelity between two quantum circuits.

        Parameters:
        circuit1 (QuantumCircuit): The first quantum circuit.
        circuit2 (QuantumCircuit): The second quantum circuit.

        Returns:
        float: The fidelity between the two circuits.
        """
        # Get the state vectors for both circuits
        state1 = Statevector.from_dict(circuit1)
        state2 = Statevector.from_dict(circuit2)
        return fidelity(state1, state2)

    def count_gates(self, circuit):
        """
        Count the number of gates in a quantum circuit.

        Parameters:
        circuit (QuantumCircuit): The quantum circuit to evaluate.

        Returns:
        int: The total number of gates in the circuit.
        """
        return circuit.size()

    def execute_circuit(self, circuit, shots=1024):
        """
        Execute a quantum circuit on the specified backend and measure execution time.

        Parameters:
        circuit (QuantumCircuit): The quantum circuit to execute.
        shots (int): The number of shots for the execution.

        Returns:
        dict: The counts of measurement outcomes.
        float: The execution time in seconds.
        """
        # Transpile the circuit for the backend
        transpiled_circuit = transpile(circuit, self.backend)
        
        # Measure execution time
        start_time = time.time()
        job = execute(transpiled_circuit, self.backend, shots=shots)
        result = job.result()
        execution_time = time.time() - start_time
        
        # Get counts of measurement outcomes
        counts = result.get_counts(transpiled_circuit)
        return counts, execution_time

    def evaluate_circuit(self, circuit1, circuit2, shots=1024):
        """
        Evaluate the quality of two quantum circuits.

        Parameters:
        circuit1 (QuantumCircuit): The first quantum circuit.
        circuit2 (QuantumCircuit): The second quantum circuit.
        shots (int): The number of shots for execution.

        Returns:
        dict: A dictionary containing fidelity, gate count, and execution time.
        """
        fidelity_value = self.calculate_fidelity(circuit1, circuit2)
        gate_count = self.count_gates(circuit1)
        counts, execution_time = self.execute_circuit(circuit1, shots)

        return {
            'fidelity': fidelity_value,
            'gate_count': gate_count,
            'execution_time': execution_time,
            'counts': counts
        }

# Example usage:
# evaluator = CircuitEvaluator()
# circuit1 = QuantumCircuit(2)
# circuit1.h(0)
# circuit1.cx(0, 1)
# circuit2 = QuantumCircuit(2)
# circuit2.h(0)
# circuit2.cx(0, 1)
# results = evaluator.evaluate_circuit(circuit1, circuit2)
# print(results)

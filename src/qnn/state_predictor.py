# src/qnn/state_predictor.py

import numpy as np
from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QuantumStatePredictor:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.backend = Aer.get_backend('statevector_simulator')

    def create_circuit(self, parameters, gates=None):
        """Create a quantum circuit based on input parameters and optional gates."""
        circuit = QuantumCircuit(self.num_qubits)

        # Apply specified gates
        if gates:
            for gate in gates:
                if gate['type'] == 'ry':
                    circuit.ry(parameters[gate['qubit']], gate['qubit'])
                elif gate['type'] == 'h':
                    circuit.h(gate['qubit'])
                elif gate['type'] == 'cx':
                    circuit.cx(gate['control'], gate['target'])
                else:
                    logging.warning(f"Unknown gate type: {gate['type']}")

        circuit.measure_all()
        return circuit

    def predict(self, parameters, gates=None):
        """Predict the quantum state based on input parameters and gates."""
        try:
            circuit = self.create_circuit(parameters, gates)
            transpiled_circuit = transpile(circuit, self.backend)
            qobj = assemble(transpiled_circuit)
            result = execute(qobj, self.backend).result()
            statevector = result.get_statevector()
            logging.info("Prediction successful.")
            return statevector
        except Exception as e:
            logging.error(f"Error during prediction: {e}")
            raise

    def evaluate(self, parameters, gates=None):
        """Evaluate the prediction and return the probabilities."""
        statevector = self.predict(parameters, gates)
        probabilities = np.abs(statevector) ** 2
        return probabilities

    def visualize_circuit(self, parameters, gates=None):
        """Visualize the quantum circuit."""
        circuit = self.create_circuit(parameters, gates)
        circuit.draw('mpl')  # Draw the circuit using Matplotlib
        plt.show()

    def prepare_bell_state(self):
        """Prepare a Bell state (entangled state)."""
        circuit = QuantumCircuit(2)
        circuit.h(0)  # Apply Hadamard gate to the first qubit
        circuit.cx(0, 1)  # Apply CNOT gate
        circuit.measure_all()
        return circuit

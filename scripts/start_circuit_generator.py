# start_circuit_generator.py

from flask import Flask, request, jsonify
import pennylane as qml
import numpy as np
import json
from typing import List, Dict
from sklearn.preprocessing import StandardScaler

# Initialize Flask app
app = Flask(__name__)

# Global variable to store generated circuits
generated_circuits = []

# Function to create a quantum circuit based on user-defined parameters
def create_quantum_circuit(num_qubits: int, gates: List[Dict[str, any]]):
    @qml.qnode(qml.device('default.qubit', wires=num_qubits))
    def circuit(params):
        # Prepare the input state
        for i in range(num_qubits):
            qml.Hadamard(wires=i)  # Initialize with Hadamard gates

        # Apply user-defined gates
        for gate in gates:
            gate_type = gate['type']
            wires = gate['wires']
            if gate_type == 'RX':
                qml.RX(params[gate['param_index']], wires=wires)
            elif gate_type == 'RY':
                qml.RY(params[gate['param_index']], wires=wires)
            elif gate_type == 'CNOT':
                qml.CNOT(wires=wires)
            elif gate_type == 'CZ':
                qml.CZ(wires=wires)
            elif gate_type == 'PauliX':
                qml.PauliX(wires=wires)
            elif gate_type == 'PauliZ':
                qml.PauliZ(wires=wires)
            # Add more gates as needed

        return qml.expval(qml.PauliZ(0))  # Default return value

    return circuit

# Route to generate a quantum circuit
@app.route('/generate_circuit', methods=['POST'])
def generate_circuit():
    data = request.json
    num_qubits = data.get('num_qubits', 2)
    gates = data.get('gates', [])

    # Create the quantum circuit
    circuit = create_quantum_circuit(num_qubits, gates)
    generated_circuits.append(circuit)

    return jsonify({'status': 'Circuit generated successfully', 'num_qubits': num_qubits, 'gates': gates})

# Route to execute the generated circuit
@app.route('/execute_circuit', methods=['POST'])
def execute_circuit():
    if not generated_circuits:
        return jsonify({'status': 'No circuits available for execution.'}), 400

    params = request.json.get('params', [])
    circuit = generated_circuits[-1]  # Execute the most recently generated circuit

    # Execute the circuit
    result = circuit(params)
    return jsonify({'result': result})

# Route to get the list of generated circuits
@app.route('/circuits', methods=['GET'])
def get_circuits():
    return jsonify({'circuits': [str(circuit) for circuit in generated_circuits]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)

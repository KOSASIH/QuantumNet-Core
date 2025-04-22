# start_cosmic_noise.py

from flask import Flask, request, jsonify
import numpy as np
import pennylane as qml
from typing import List, Dict
import random

# Initialize Flask app
app = Flask(__name__)

# Function to create a quantum circuit with noise
def create_noisy_circuit(num_qubits: int, noise_level: float):
    @qml.qnode(qml.device('default.qubit', wires=num_qubits))
    def circuit(params):
        # Prepare the input state
        for i in range(num_qubits):
            qml.Hadamard(wires=i)  # Initialize with Hadamard gates

        # Apply parameterized gates with noise
        for i in range(num_qubits):
            qml.RX(params[i], wires=i)
            if random.random() < noise_level:
                qml.DepolarizingChannel(0.1, wires=i)  # Apply depolarizing noise

        return qml.expval(qml.PauliZ(0))  # Default return value

    return circuit

# Route to generate a noisy quantum circuit
@app.route('/generate_noisy_circuit', methods=['POST'])
def generate_noisy_circuit():
    data = request.json
    num_qubits = data.get('num_qubits', 2)
    noise_level = data.get('noise_level', 0.1)

    # Create the noisy quantum circuit
    circuit = create_noisy_circuit(num_qubits, noise_level)

    return jsonify({'status': 'Noisy circuit generated successfully', 'num_qubits': num_qubits, 'noise_level': noise_level})

# Route to execute the noisy circuit
@app.route('/execute_noisy_circuit', methods=['POST'])
def execute_noisy_circuit():
    data = request.json
    params = data.get('params', [])
    num_qubits = data.get('num_qubits', 2)
    noise_level = data.get('noise_level', 0.1)

    # Create the noisy circuit
    circuit = create_noisy_circuit(num_qubits, noise_level)

    # Execute the circuit
    result = circuit(params)
    return jsonify({'result': result})

# Route to evaluate noise resilience
@app.route('/evaluate_resilience', methods=['POST'])
def evaluate_resilience():
    data = request.json
    num_trials = data.get('num_trials', 100)
    num_qubits = data.get('num_qubits', 2)
    noise_level = data.get('noise_level', 0.1)
    params = data.get('params', [0.5] * num_qubits)

    success_count = 0

    for _ in range(num_trials):
        circuit = create_noisy_circuit(num_qubits, noise_level)
        result = circuit(params)
        if result > 0:  # Assuming positive result indicates success
            success_count += 1

    resilience = success_count / num_trials
    return jsonify({'resilience': resilience})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)

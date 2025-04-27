import numpy as np
import json
from qiskit import QuantumCircuit, Aer, execute

def create_random_quantum_state(n_qubits):
    """Create a random quantum state."""
    circuit = QuantumCircuit(n_qubits)
    for qubit in range(n_qubits):
        circuit.h(qubit)  # Apply Hadamard gate to create superposition
    backend = Aer.get_backend('statevector_simulator')
    result = execute(circuit, backend).result()
    statevector = result.get_statevector()
    return statevector

def generate_temporal_states(num_states, n_qubits):
    """Generate synthetic temporal quantum states."""
    states = []
    for i in range(num_states):
        state = create_random_quantum_state(n_qubits)
        states.append({
            'id': i,
            'state_vector': state.tolist(),  # Convert to list for JSON serialization
            'timestamp': f"2023-10-01T00:00:0{i}:00Z",  # Example timestamp
            'entanglement': np.random.uniform(0, 1)  # Random entanglement measure
        })
    return states

def save_temporal_states_to_json(states, filename):
    """Save the generated states to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(states, f, indent=4)

def main():
    num_states = 100  # Number of synthetic states to generate
    n_qubits = 3  # Number of qubits for each state
    states = generate_temporal_states(num_states, n_qubits)
    save_temporal_states_to_json(states, 'temporal/temporal_states.json')
    print(f"Generated {num_states} temporal quantum states and saved to 'temporal/temporal_states.json'.")

if __name__ == "__main__":
    main()

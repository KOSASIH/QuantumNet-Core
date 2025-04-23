# protocol_example.py

import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit.quantum_info import Statevector

def create_teleportation_circuit():
    # Create a Quantum Circuit with 3 qubits and 2 classical bits
    circuit = QuantumCircuit(3, 2)

    # Step 1: Create entanglement between qubit 1 and qubit 2
    circuit.h(1)  # Apply Hadamard gate to qubit 1
    circuit.cx(1, 2)  # Apply CNOT gate to entangle qubit 1 and qubit 2

    return circuit

def teleport_state(circuit, state):
    # Step 2: Prepare the state to be teleported (qubit 0)
    circuit.initialize(state, 0)

    # Step 3: Bell measurement
    circuit.cx(0, 1)  # Apply CNOT gate
    circuit.h(0)  # Apply Hadamard gate
    circuit.measure(0, 0)  # Measure qubit 0
    circuit.measure(1, 1)  # Measure qubit 1

    # Step 4: Apply corrections based on measurement results
    circuit.x(2).c_if(0, 1)  # Apply X gate if measurement of qubit 0 is 1
    circuit.z(2).c_if(1, 1)  # Apply Z gate if measurement of qubit 1 is 1

    return circuit

def main():
    # Define the state to be teleported (e.g., |+⟩ state)
    state = [1/np.sqrt(2), 1/np.sqrt(2)]  # |+⟩ = (|0⟩ + |1⟩) / √2

    # Create the teleportation circuit
    circuit = create_teleportation_circuit()

    # Teleport the state
    teleport_circuit = teleport_state(circuit, state)

    # Execute the circuit on a quantum simulator
    backend = Aer.get_backend('qasm_simulator')
    job = execute(teleport_circuit, backend, shots=1024)
    result = job.result()

    # Get the measurement results
    counts = result.get_counts(teleport_circuit)
    print("Measurement results:", counts)

    # Visualize the results
    plot_histogram(counts).show()

    # Verify the final state of the teleported qubit
    final_state = Statevector.from_dict(counts)
    print("Final state of the teleported qubit:", final_state)

    # Visualize the final state on the Bloch sphere
    plot_bloch_multivector(final_state).show()

if __name__ == "__main__":
    main()

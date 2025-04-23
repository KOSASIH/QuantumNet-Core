# qec_example.py

import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector

def create_shor_code_circuit():
    # Create a Quantum Circuit with 9 qubits (for Shor's code)
    circuit = QuantumCircuit(9, 1)

    # Step 1: Encode the logical qubit |ψ⟩ = |0⟩
    circuit.h(0)  # Start with |+⟩ state
    circuit.cx(0, 1)
    circuit.cx(0, 2)

    # Step 2: Create entanglement for error correction
    circuit.cx(1, 3)
    circuit.cx(1, 4)
    circuit.cx(2, 5)
    circuit.cx(2, 6)

    # Step 3: Apply Hadamard gates to create superposition
    circuit.h(3)
    circuit.h(4)
    circuit.h(5)
    circuit.h(6)

    return circuit

def introduce_errors(circuit):
    # Introduce errors to the encoded qubits
    circuit.x(1)  # Introduce an X error on qubit 1
    circuit.z(3)  # Introduce a Z error on qubit 3

def decode_and_correct(circuit):
    # Step 4: Measure the qubits to detect errors
    circuit.measure(3, 0)  # Measure qubit 3
    circuit.measure(4, 1)  # Measure qubit 4
    circuit.measure(5, 2)  # Measure qubit 5
    circuit.measure(6, 3)  # Measure qubit 6

    # Step 5: Apply correction based on measurement results
    circuit.x(1).c_if(0, 1)  # Apply X correction if measurement of qubit 3 is 1
    circuit.z(0).c_if(1, 1)  # Apply Z correction if measurement of qubit 4 is 1

def main():
    # Create the Shor code circuit
    circuit = create_shor_code_circuit()

    # Introduce errors
    introduce_errors(circuit)

    # Decode and correct the errors
    decode_and_correct(circuit)

    # Execute the circuit on a quantum simulator
    backend = Aer.get_backend('qasm_simulator')
    job = execute(circuit, backend, shots=1024)
    result = job.result()

    # Get the measurement results
    counts = result.get_counts(circuit)
    print("Measurement results:", counts)

    # Visualize the results
    plot_histogram(counts).show()

if __name__ == "__main__":
    main()

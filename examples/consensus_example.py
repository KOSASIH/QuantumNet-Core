# consensus_example.py

import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram

def create_voting_circuit(votes):
    # Create a Quantum Circuit with 3 qubits (for 3 voters)
    circuit = QuantumCircuit(3, 3)

    # Step 1: Initialize the qubits based on the votes
    for i, vote in enumerate(votes):
        if vote == 1:
            circuit.x(i)  # Apply X gate for a 'yes' vote

    # Step 2: Apply CNOT gates to create entanglement
    circuit.cx(0, 1)
    circuit.cx(0, 2)

    # Step 3: Measure the qubits
    circuit.measure(range(3), range(3))

    return circuit

def main():
    # Define the votes from 3 voters (1 for 'yes', 0 for 'no')
    votes = [1, 0, 1]  # Voter 1 and Voter 3 vote 'yes', Voter 2 votes 'no'

    # Create the voting circuit
    circuit = create_voting_circuit(votes)

    # Execute the circuit on a quantum simulator
    backend = Aer.get_backend('qasm_simulator')
    job = execute(circuit, backend, shots=1024)
    result = job.result()

    # Get the measurement results
    counts = result.get_counts(circuit)
    print("Measurement results:", counts)

    # Visualize the results
    plot_histogram(counts).show()

    # Determine the consensus based on the majority vote
    majority_vote = max(counts, key=lambda x: counts[x])
    print(f"Consensus result: {majority_vote}")

if __name__ == "__main__":
    main()

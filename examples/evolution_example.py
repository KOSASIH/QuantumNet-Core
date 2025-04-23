### `evolution_example.py`

import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector

def create_hamiltonian_evolution_circuit(theta):
    # Create a Quantum Circuit with 1 qubit
    circuit = QuantumCircuit(1)

    # Apply a rotation around the Y-axis based on the Hamiltonian
    circuit.ry(theta, 0)  # Rotate the qubit state

    return circuit

def main():
    # Define parameters for evolution
    time_steps = 100
    theta_values = np.linspace(0, 2 * np.pi, time_steps)  # Evolve from 0 to 2π

    # Initialize the state vector
    initial_state = Statevector.from_dict({'0': 1, '1': 0})  # Start in |0⟩ state

    # Prepare to store the evolved states
    evolved_states = []

    for theta in theta_values:
        # Create the Hamiltonian evolution circuit
        circuit = create_hamiltonian_evolution_circuit(theta)

        # Get the evolved state
        evolved_state = initial_state.evolve(circuit)
        evolved_states.append(evolved_state)

    # Visualize the evolution on the Bloch sphere
    plot_bloch_multivector(evolved_states[-1]).show()

    # Print the final state
    print("Final state vector:", evolved_states[-1])

if __name__ == "__main__":
    main()

"""
AQCG Utilities for Quantum Circuit Generation and Evaluation
"""
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram, plot_state_qsphere
from qiskit.quantum_info import Statevector

def visualize_circuit(circuit: QuantumCircuit, filename=None):
    """
    Visualize a quantum circuit.

    Parameters:
    circuit (QuantumCircuit): The quantum circuit to visualize.
    filename (str): Optional filename to save the visualization as an image.
    """
    circuit.draw('mpl', filename=filename)
    print(f"Circuit visualized and saved to {filename}" if filename else "Circuit visualized.")

def plot_histogram_data(counts, title='Measurement Outcomes'):
    """
    Plot a histogram of measurement outcomes.

    Parameters:
    counts (dict): The counts of measurement outcomes.
    title (str): Title of the histogram plot.
    """
    plot_histogram(counts)
    plt.title(title)
    plt.show()

def plot_state_vector(state_vector: Statevector, title='Quantum State Vector'):
    """
    Plot the quantum state vector on a Q-sphere.

    Parameters:
    state_vector (Statevector): The quantum state vector to visualize.
    title (str): Title of the Q-sphere plot.
    """
    plot_state_qsphere(state_vector)
    plt.title(title)
    plt.show()

def circuit_to_matrix(circuit: QuantumCircuit):
    """
    Convert a quantum circuit to its matrix representation.

    Parameters:
    circuit (QuantumCircuit): The quantum circuit to convert.

    Returns:
    np.ndarray: The matrix representation of the circuit.
    """
    return circuit.to_matrix()

def matrix_to_circuit(matrix: np.ndarray):
    """
    Convert a unitary matrix to a quantum circuit.

    Parameters:
    matrix (np.ndarray): The unitary matrix to convert.

    Returns:
    QuantumCircuit: The corresponding quantum circuit.
    """
    from qiskit.circuit.library import UnitaryGate
    return QuantumCircuit.from_gate(UnitaryGate(matrix))

def random_unitary(n_qubits):
    """
    Generate a random unitary matrix of size 2^n_qubits x 2^n_qubits.

    Parameters:
    n_qubits (int): Number of qubits.

    Returns:
    np.ndarray: A random unitary matrix.
    """
    # Generate a random unitary matrix using QR decomposition
    random_matrix = np.random.rand(2**n_qubits, 2**n_qubits) + 1j * np.random.rand(2**n_qubits, 2**n_qubits)
    q, r = np.linalg.qr(random_matrix)
    return q @ np.diag(np.sign(np.diag(r)))

def fidelity(state1, state2):
    """
    Calculate the fidelity between two quantum states.

    Parameters:
    state1 (Statevector or np.ndarray): The first quantum state.
    state2 (Statevector or np.ndarray): The second quantum state.

    Returns:
    float: The fidelity between the two states.
    """
    if isinstance(state1, Statevector):
        state1 = state1.data
    if isinstance(state2, Statevector):
        state2 = state2.data
    return np.abs(np.dot(state1.conj(), state2))**2

def normalize_vector(vector):
    """
    Normalize a vector.

    Parameters:
    vector (np.ndarray): The vector to normalize.

    Returns:
    np.ndarray: The normalized vector.
    """
    norm = np.linalg.norm(vector)
    if norm == 0:
        raise ValueError("Cannot normalize a zero vector.")
    return vector / norm

# Example usage:
# circuit = QuantumCircuit(2)
# circuit.h(0)
# circuit.cx(0, 1)
# visualize_circuit(circuit)
# counts = {'00': 500, '01': 300, '10': 200}
# plot_histogram_data(counts)
# state_vector = Statevector.from_dict({'00': 1, '01': 0, '10': 0, '11': 0})
# plot_state_vector(state_vector)

"""
Utilities for Quantum Cosmic Memory Fabric (QCMF).
"""
import numpy as np
from qiskit.quantum_info import Statevector
from typing import List, Tuple

def generate_random_state(n_qubits: int) -> np.ndarray:
    """
    Generate a random quantum state for a given number of qubits.

    Args:
        n_qubits (int): Number of qubits.

    Returns:
        np.ndarray: Randomly generated quantum state.
    """
    state = Statevector.from_dict({(0,)*n_qubits: 1})  # Start with |0...0>
    random_state = state.evolve(Statevector.random(2**n_qubits))
    return random_state.to_vector()

def validate_state(state: np.ndarray) -> bool:
    """
    Validate a quantum state.

    Args:
        state (np.ndarray): Quantum state to validate.

    Returns:
        bool: True if the state is valid, False otherwise.
    """
    norm = np.linalg.norm(state)
    return np.isclose(norm, 1.0)

def normalize_state(state: np.ndarray) -> np.ndarray:
    """
    Normalize a quantum state.

    Args:
        state (np.ndarray): Quantum state to normalize.

    Returns:
        np.ndarray: Normalized quantum state.
    """
    norm = np.linalg.norm(state)
    if norm == 0:
        raise ValueError("Cannot normalize a zero vector.")
    return state / norm

def encode_classical_data(data: List[float]) -> np.ndarray:
    """
    Encode classical data into a quantum state.

    Args:
        data (List[float]): Classical data to encode.

    Returns:
        np.ndarray: Quantum state representing the classical data.
    """
    if len(data) == 0:
        raise ValueError("Data cannot be empty.")
    normalized_data = normalize_state(np.array(data))
    return normalized_data

def decode_quantum_state(state: np.ndarray) -> List[float]:
    """
    Decode a quantum state back into classical data.

    Args:
        state (np.ndarray): Quantum state to decode.

    Returns:
        List[float]: Classical data representation of the quantum state.
    """
    return state.tolist()

def calculate_inner_product(state1: np.ndarray, state2: np.ndarray) -> complex:
    """
    Calculate the inner product of two quantum states.

    Args:
        state1 (np.ndarray): First quantum state.
        state2 (np.ndarray): Second quantum state.

    Returns:
        complex: Inner product of the two states.
    """
    return np.vdot(state1, state2)

def measure_state(state: np.ndarray) -> int:
    """
    Measure a quantum state and return the result.

    Args:
        state (np.ndarray): Quantum state to measure.

    Returns:
        int: Measurement result (0 or 1).
    """
    probabilities = np.abs(state)**2
    return np.random.choice(len(state), p=probabilities)

# Example usage
if __name__ == "__main__":
    n_qubits = 3
    random_state = generate_random_state(n_qubits)
    print("Random Quantum State:", random_state)

    if validate_state(random_state):
        print("The state is valid.")

    normalized_state = normalize_state(random_state)
    print("Normalized Quantum State:", normalized_state)

    classical_data = [1, 0, 0, 1]
    encoded_state = encode_classical_data(classical_data)
    print("Encoded Quantum State:", encoded_state)

    decoded_data = decode_quantum_state(encoded_state)
    print("Decoded Classical Data:", decoded_data)

    inner_product = calculate_inner_product(random_state, normalized_state)
    print("Inner Product:", inner_product)

    measurement_result = measure_state(normalized_state)
    print("Measurement Result:", measurement_result)

"""
Utility Functions for Cosmic Noise Reduction and Error Correction (CNRE)
"""
import numpy as np
from qiskit.quantum_info import Statevector, Operator

def apply_noise(state: Statevector, noise_type: str, noise_level: float) -> Statevector:
    """
    Apply noise to a quantum state.

    Parameters:
    state (Statevector): The original quantum state.
    noise_type (str): Type of noise to apply ('depolarizing', 'bit_flip', 'phase_flip').
    noise_level (float): Level of noise to apply (0 to 1).

    Returns:
    Statevector: The noisy quantum state.
    """
    if noise_type == 'depolarizing':
        return apply_depolarizing_noise(state, noise_level)
    elif noise_type == 'bit_flip':
        return apply_bit_flip_noise(state, noise_level)
    elif noise_type == 'phase_flip':
        return apply_phase_flip_noise(state, noise_level)
    else:
        raise ValueError("Invalid noise type specified.")

def apply_depolarizing_noise(state: Statevector, noise_level: float) -> Statevector:
    """Apply depolarizing noise to a quantum state."""
    num_qubits = int(np.log2(len(state)))
    noise_matrix = (1 - noise_level) * np.eye(2**num_qubits) + (noise_level / (3 * (2**num_qubits - 1))) * (np.kron(np.eye(2**(num_qubits-1)), np.array([[0, 1], [1, 0]])) +
                                                                                                           np.kron(np.eye(2**(num_qubits-1)), np.array([[1, 0], [0, -1]])) +
                                                                                                           np.kron(np.eye(2**(num_qubits-1)), np.array([[0, -1j], [1j, 0]])))
    return Operator(noise_matrix).dot(state)

def apply_bit_flip_noise(state: Statevector, noise_level: float) -> Statevector:
    """Apply bit-flip noise to a quantum state."""
    num_qubits = int(np.log2(len(state)))
    for i in range(num_qubits):
        if np.random.rand() < noise_level:
            state = Operator(np.array([[0, 1], [1, 0]])).dot(state)
    return state

def apply_phase_flip_noise(state: Statevector, noise_level: float) -> Statevector:
    """Apply phase-flip noise to a quantum state."""
    num_qubits = int(np.log2(len(state)))
    for i in range(num_qubits):
        if np.random.rand() < noise_level:
            state = Operator(np.array([[1, 0], [0, -1]])).dot(state)
    return state

def calculate_fidelity(state1: Statevector, state2: Statevector) -> float:
    """
    Calculate the fidelity between two quantum states.

    Parameters:
    state1 (Statevector): The first quantum state.
    state2 (Statevector): The second quantum state.

    Returns:
    float: The fidelity between the two states.
    """
    return np.abs(np.dot(state1, state2)) ** 2

def preprocess_data(data: np.ndarray) -> np.ndarray:
    """
    Preprocess data for training or evaluation.

    Parameters:
    data (np.ndarray): The raw data to preprocess.

    Returns:
    np.ndarray: The preprocessed data.
    """
    # Normalize the data
    return data / np.linalg.norm(data)

def generate_noisy_states(original_states: np.ndarray, noise_type: str, noise_level: float) -> np.ndarray:
    """
    Generate a set of noisy quantum states from original states.

    Parameters:
    original_states (np.ndarray): Array of original quantum states.
    noise_type (str): Type of noise to apply.
    noise_level (float): Level of noise to apply.

    Returns:
    np.ndarray: Array of noisy quantum states.
    """
    noisy_states = []
    for state in original_states:
        noisy_state = apply_noise(Statevector(state), noise_type, noise_level)
        noisy_states.append(noisy_state)
    return np.array(noisy_states)

def visualize_state(state: Statevector, title: str = "Quantum State"):
    """
    Visualize a quantum state using a Q-sphere.

    Parameters:
    state (Statevector): The quantum state to visualize.
    title (str): Title for the visualization.
    """
    from qiskit.visualization import plot_state_qsphere
    plot_state_qsphere(state)
    plt.title(title)
    plt .show()  # Display the Q-sphere visualization

# Example usage:
# original_state = Statevector.from_dict({'00': 1, '01': 0, '10': 0, '11': 0})
# noisy_state = apply_noise(original_state, noise_type='depolarizing', noise_level=0.1)
# fidelity = calculate_fidelity(original_state, noisy_state)
# print("Fidelity:", fidelity)
# noisy_states = generate_noisy_states(np.array([original_state]), noise_type='bit_flip', noise_level=0.2)
# visualize_state(noisy_states[0], title="Noisy Quantum State")

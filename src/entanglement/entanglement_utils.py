# entanglement/entanglement_utils.py

import numpy as np

def normalize_state(state):
    """Normalizes a quantum state vector.
    
    Args:
        state (np.ndarray): The quantum state vector to normalize.

    Returns:
        np.ndarray: The normalized quantum state vector.

    Raises:
        ValueError: If the input state is a zero vector.
    """
    norm = np.linalg.norm(state)
    if norm == 0:
        raise ValueError("Cannot normalize a zero vector.")
    return state / norm

def inner_product(state1, state2):
    """Calculates the inner product of two quantum states.
    
    Args:
        state1 (np.ndarray): The first quantum state vector.
        state2 (np.ndarray): The second quantum state vector.

    Returns:
        complex: The inner product of the two quantum states.
    """
    return np.vdot(state1, state2)

def fidelity(state1, state2):
    """Calculates the fidelity between two quantum states.
    
    Fidelity is a measure of the "closeness" of two quantum states.
    
    Args:
        state1 (np.ndarray): The first quantum state vector.
        state2 (np.ndarray): The second quantum state vector.

    Returns:
        float: The fidelity between the two quantum states.
    """
    state1 = normalize_state(state1)
    state2 = normalize_state(state2)
    return np.abs(inner_product(state1, state2))**2

def tensor_product(state1, state2):
    """Calculates the tensor product of two quantum states.
    
    Args:
        state1 (np.ndarray): The first quantum state vector.
        state2 (np.ndarray): The second quantum state vector.

    Returns:
        np.ndarray: The tensor product of the two quantum states.
    """
    return np.kron(state1, state2)

def partial_trace(density_matrix, subsystem):
    """Calculates the partial trace of a density matrix over a specified subsystem.
    
    Args:
        density_matrix (np.ndarray): The density matrix to trace over.
        subsystem (int): The subsystem index to trace out (0 or 1).

    Returns:
        np.ndarray: The reduced density matrix after tracing out the specified subsystem.
    """
    if subsystem not in [0, 1]:
        raise ValueError("Subsystem must be 0 or 1.")
    
    dim = int(np.sqrt(density_matrix.shape[0]))  # Assuming square density matrix
    if subsystem == 0:
        return np.trace(density_matrix.reshape(dim, dim, dim, dim), axis1=0, axis2=2)
    else:
        return np.trace(density_matrix.reshape(dim, dim, dim, dim), axis1=1, axis2=3)

def is_orthogonal(state1, state2):
    """Checks if two quantum states are orthogonal.
    
    Args:
        state1 (np.ndarray): The first quantum state vector.
        state2 (np.ndarray): The second quantum state vector.

    Returns:
        bool: True if the states are orthogonal, False otherwise.
    """
    return np.isclose(inner_product(state1, state2), 0)

# Example usage
if __name__ == "__main__":
    state_a = np.array([1, 0, 0, 0])  # |0⟩ state
    state_b = np.array([0, 1, 0, 0])  # |1⟩ state

    print("Normalized State A:", normalize_state(state_a))
    print("Inner Product:", inner_product(state_a, state_b))
    print("Fidelity:", fidelity(state_a, state_b))
    print("Tensor Product:", tensor_product(state_a, state_b))
    print("Are states orthogonal?", is_orthogonal(state_a, state_b))

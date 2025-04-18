import numpy as np

def random_bit_string(length):
    """Generate a random bit string of a given length using a secure random generator."""
    return np.random.randint(0, 2, length).tolist()

def measure_qubit(state, basis):
    """Measure a qubit in a given basis.
    
    Parameters:
    - state (np.ndarray): The quantum state vector (should be normalized).
    - basis (str): The measurement basis ('Z' or 'X').
    
    Returns:
    - int: The measurement result (0 or 1).
    """
    if basis not in ['Z', 'X']:
        raise ValueError("Invalid basis. Choose 'Z' or 'X'.")

    if basis == 'Z':
        probabilities = np.abs(state)**2
        result = np.random.choice([0, 1], p=probabilities)
    elif basis == 'X':
        # Transform to X basis
        state_x = np.array([state[0] + state[1], state[0] - state[1]]) / np.sqrt(2)
        probabilities = np.abs(state_x)**2
        result = np.random.choice([0, 1], p=probabilities)

    return result

def prepare_state(state_type):
    """Prepare a common quantum state.
    
    Parameters:
    - state_type (str): The type of state to prepare ('0', '1', '+', '-').
    
    Returns:
    - np.ndarray: The prepared quantum state vector.
    """
    if state_type == '0':
        return np.array([1, 0])  # |0>
    elif state_type == '1':
        return np.array([0, 1])  # |1>
    elif state_type == '+':
        return np.array([1/np.sqrt(2), 1/np.sqrt(2)])  # |+>
    elif state_type == '-':
        return np.array([1/np.sqrt(2), -1/np.sqrt(2)])  # |->
    else:
        raise ValueError("Invalid state type. Choose '0', '1', '+', or '-'.")

def apply_pauli_x(state):
    """Apply the Pauli-X gate (bit-flip) to a qubit state.
    
    Parameters:
    - state (np.ndarray): The quantum state vector.
    
    Returns:
    - np.ndarray: The resulting quantum state after applying the Pauli-X gate.
    """
    return np.array([state[1], state[0]])

def apply_pauli_z(state):
    """Apply the Pauli-Z gate (phase-flip) to a qubit state.
    
    Parameters:
    - state (np.ndarray): The quantum state vector.
    
    Returns:
    - np.ndarray: The resulting quantum state after applying the Pauli-Z gate.
    """
    return np.array([state[0], -state[1]])

def apply_hadamard(state):
    """Apply the Hadamard gate to a qubit state.
    
    Parameters:
    - state (np.ndarray): The quantum state vector.
    
    Returns:
    - np.ndarray: The resulting quantum state after applying the Hadamard gate.
    """
    return np.array([state[0] + state[1], state[0] - state[1]]) / np.sqrt(2)

# Example usage
if __name__ == "__main__":
    # Prepare a quantum state
    state = prepare_state('+')
    print("Initial State:", state)

    # Measure the state in Z basis
    measurement_result_z = measure_qubit(state, 'Z')
    print("Measurement Result in Z basis:", measurement_result_z)

    # Apply Pauli-X gate
    new_state = apply_pauli_x(state)
    print("State after Pauli-X:", new_state)

    # Measure the new state in X basis
    measurement_result_x = measure_qubit(new_state, 'X')
    print("Measurement Result in X basis:", measurement_result_x)

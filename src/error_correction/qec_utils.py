import numpy as np
import matplotlib.pyplot as plt
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_random_errors(size, error_rate, error_type='bit_flip'):
    """Generate random errors for a given size and error rate.
    
    Parameters:
    - size (int): The size of the qubit array (size x size).
    - error_rate (float): The probability of an error occurring at each qubit.
    - error_type (str): The type of error to generate ('bit_flip', 'phase_flip', 'depolarizing').
    
    Returns:
    - np.ndarray: An array representing the errors.
    """
    errors = np.random.rand(size, size) < error_rate
    if error_type == 'bit_flip':
        return errors.astype(int)
    elif error_type == 'phase_flip':
        return errors.astype(int) * 2  # Represent phase flip with a different value
    elif error_type == 'depolarizing':
        return np.random.choice([0, 1, 2], size=(size, size), p=[1 - error_rate, error_rate / 2, error_rate / 2])
    else:
        raise ValueError("Invalid error type. Choose 'bit_flip', 'phase_flip', or 'depolarizing'.")

def apply_errors(qubits, errors):
    """Apply errors to the qubits.
    
    Parameters:
    - qubits (np.ndarray): The original qubit states.
    - errors (np.ndarray): The errors to apply.
    
    Returns:
    - np.ndarray: The corrupted qubit states.
    """
    corrupted_qubits = qubits.copy()
    bit_flip_mask = (errors == 1)
    phase_flip_mask = (errors == 2)

    # Apply bit-flip errors
    corrupted_qubits[bit_flip_mask] ^= 1  # Flip qubits where bit-flip errors are present

    # Apply phase-flip errors (for demonstration, we can just log it)
    if np.any(phase_flip_mask):
        logging.info("Phase flip errors applied at positions: %s", np.argwhere(phase_flip_mask))

    return corrupted_qubits

def calculate_error_rate(original, corrupted):
    """Calculate the error rate between original and corrupted states.
    
    Parameters:
    - original (np.ndarray): The original qubit states.
    - corrupted (np.ndarray): The corrupted qubit states.
    
    Returns:
    - float: The error rate.
    """
    return np.sum(original != corrupted) / original.size

def visualize_states(original, corrupted):
    """Visualize the original and corrupted qubit states.
    
    Parameters:
    - original (np.ndarray): The original qubit states.
    - corrupted (np.ndarray): The corrupted qubit states.
    """
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(original, cmap='gray', interpolation='nearest')
    axes[0].set_title('Original State')
    axes[0].axis('off')

    axes[1].imshow(corrupted, cmap='gray', interpolation='nearest')
    axes[1].set_title('Corrupted State')
    axes[1].axis('off')

    plt.show()

# Example usage
if __name__ == "__main__":
    original_state = np.array([[0, 1], [1, 0]])
    error_rate = 0.1
    errors = generate_random_errors(2, error_rate, error_type='depolarizing')
    corrupted_state = apply_errors(original_state, errors)
    error_rate_calculated = calculate_error_rate(original_state, corrupted_state)

    print("Original State:\n", original_state)
    print("Errors Applied:\n", errors)
    print("Corrupted State:\n", corrupted_state)
    print("Calculated Error Rate:", error_rate_calculated)

    # Visualize the states
    visualize_states(original_state, corrupted_state)

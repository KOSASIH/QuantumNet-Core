# quantum_state/state_vector.py

import numpy as np

class StateVector:
    """Class representing a quantum state using a state vector."""
    
    def __init__(self, amplitudes):
        """Initializes the state vector with given amplitudes.
        
        Args:
            amplitudes (list or np.ndarray): The amplitudes of the quantum state.
        """
        self.amplitudes = np.array(amplitudes, dtype=complex)
        self.normalize()

    def normalize(self):
        """Normalizes the quantum state vector.
        
        Raises:
            ValueError: If the vector is a zero vector.
        """
        norm = np.linalg.norm(self.amplitudes)
        if norm == 0:
            raise ValueError("Cannot normalize a zero vector.")
        self.amplitudes /= norm

    def __repr__(self):
        return f"StateVector(amplitudes={self.amplitudes})"

    def measure(self):
        """Measures the quantum state and collapses it to one of the basis states.
        
        Returns:
            int: The index of the measured basis state.
        """
        probabilities = np.abs(self.amplitudes) ** 2
        return np.random.choice(len(self.amplitudes), p=probabilities)

    def inner_product(self, other):
        """Calculates the inner product with another state vector.
        
        Args:
            other (StateVector): The other state vector to calculate the inner product with.
        
        Returns:
            complex: The inner product of the two state vectors.
        """
        if not isinstance(other, StateVector):
            raise ValueError("The other object must be a StateVector.")
        return np.vdot(self.amplitudes, other.amplitudes)

    def tensor_product(self, other):
        """Calculates the tensor product with another state vector.
        
        Args:
            other (StateVector): The other state vector to calculate the tensor product with.
        
        Returns:
            StateVector: A new StateVector representing the tensor product.
        """
        if not isinstance(other, StateVector):
            raise ValueError("The other object must be a StateVector.")
        tensor_result = np.kron(self.amplitudes, other.amplitudes)
        return StateVector(tensor_result)

    def fidelity(self, other):
        """Calculates the fidelity with another state vector.
        
        Args:
            other (StateVector): The other state vector to calculate fidelity with.
        
        Returns:
            float: The fidelity between the two state vectors.
        """
        if not isinstance(other, StateVector):
            raise ValueError("The other object must be a StateVector.")
        return np.abs(self.inner_product(other)) ** 2

# Example usage
if __name__ == "__main__":
    state1 = StateVector([1, 0, 0, 0])  # |0⟩ state
    state2 = StateVector([0, 1, 0, 0])  # |1⟩ state
    print("State 1:", state1)
    print("State 2:", state2)
    
    measurement_result = state1.measure()
    print("Measurement Result of State 1:", measurement_result)
    
    inner_prod = state1.inner_product(state2)
    print("Inner Product of State 1 and State 2:", inner_prod)
    
    tensor_prod = state1.tensor_product(state2)
    print("Tensor Product of State 1 and State 2:", tensor_prod)
    
    fidelity_value = state1.fidelity(state2)
    print("Fidelity between State 1 and State 2:", fidelity_value)

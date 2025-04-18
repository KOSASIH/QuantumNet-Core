# quantum_state/density_matrix.py

import numpy as np

class DensityMatrix:
    """Class representing a quantum state using a density matrix."""
    
    def __init__(self, matrix):
        """Initializes the density matrix with the given matrix.
        
        Args:
            matrix (list or np.ndarray): The density matrix to represent.
        """
        self.matrix = np.array(matrix, dtype=complex)
        self.validate()

    def validate(self):
        """Validates the density matrix properties.
        
        Raises:
            ValueError: If the matrix is not Hermitian or not positive semi-definite.
        """
        if not np.allclose(self.matrix, self.matrix.conj().T):
            raise ValueError("Density matrix must be Hermitian.")
        if not np.all(np.linalg.eigvals(self.matrix) >= 0):
            raise ValueError("Density matrix must be positive semi-definite.")

    def trace(self):
        """Calculates the trace of the density matrix.
        
        Returns:
            complex: The trace of the density matrix.
        """
        return np.trace(self.matrix)

    def measure(self):
        """Measures the quantum state represented by the density matrix.
        
        Returns:
            int: The index of the measured basis state.
        """
        eigenvalues, eigenvectors = np.linalg.eig(self.matrix)
        probabilities = eigenvalues / np.sum(eigenvalues)
        return np.random.choice(len(eigenvalues), p=probabilities)

    def partial_trace(self, subsystem):
        """Calculates the partial trace of the density matrix over a specified subsystem.
        
        Args:
            subsystem (int): The subsystem index to trace out (0 or 1).
        
        Returns:
            DensityMatrix: The reduced density matrix after tracing out the specified subsystem.
        """
        if subsystem not in [0, 1]:
            raise ValueError("Subsystem must be 0 or 1.")
        
        dim = int(np.sqrt(self.matrix.shape[0]))  # Assuming square density matrix
        if subsystem == 0:
            return DensityMatrix(np.trace(self.matrix.reshape(dim, dim, dim, dim), axis1=0, axis2=2))
        else:
            return DensityMatrix(np.trace(self.matrix.reshape(dim, dim, dim, dim), axis1=1, axis2=3))

    def __repr__(self):
        return f"DensityMatrix(matrix={self.matrix})"

# Example usage
if __name__ == "__main__":
    density_matrix = DensityMatrix([[1, 0], [0, 0]])  # |0⟩ state
    print("Density Matrix:\n", density_matrix)
    print("Trace:", density_matrix.trace())
    measurement_result = density_matrix.measure()
    print("Measurement Result:", measurement_result)
    
    # Example of partial trace
    combined_density_matrix = DensityMatrix([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]])  # |00⟩ + |11⟩
    reduced_density_matrix = combined_density_matrix.partial_trace(0)  # Trace out subsystem 0
    print("Reduced Density Matrix (Subsystem 0):\n", reduced_density_matrix)

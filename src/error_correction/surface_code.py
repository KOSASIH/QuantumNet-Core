import numpy as np
import matplotlib.pyplot as plt

class SurfaceCode:
    def __init__(self, size):
        self.size = size
        self.qubits = np.zeros((size, size), dtype=int)  # Initialize qubits
        self.stabilizers = []  # List to hold stabilizer measurements

    def apply_error(self, x, y):
        """Simulate an error on the qubit at position (x, y)."""
        if 0 <= x < self.size and 0 <= y < self.size:
            self.qubits[x, y] ^= 1  # Flip the qubit state (0 -> 1 or 1 -> 0)
        else:
            raise IndexError("Error position out of bounds.")

    def measure_stabilizers(self):
        """Measure the stabilizers of the surface code."""
        self.stabilizers = []  # Reset stabilizers for new measurements

        # Measure X stabilizers
        for i in range(self.size):
            for j in range(self.size):
                if (i + j) % 2 == 0:  # Check for X stabilizer positions
                    stabilizer_value = (self.qubits[i, j] ^
                                        self.qubits[i, (j + 1) % self.size] ^
                                        self.qubits[(i + 1) % self.size, j])
                    self.stabilizers.append(stabilizer_value)

        # Measure Z stabilizers
        for i in range(self.size):
            for j in range(self.size):
                if (i + j) % 2 == 1:  # Check for Z stabilizer positions
                    stabilizer_value = (self.qubits[i, j] ^
                                        self.qubits[i, (j + 1) % self.size] ^
                                        self.qubits[(i + 1) % self.size, j])
                    self.stabilizers.append(stabilizer_value)

        return self.stabilizers

    def decode_errors(self):
        """Decode the errors based on stabilizer measurements."""
        # Simple error correction logic based on stabilizer measurements
        error_correction = []
        for index, stabilizer in enumerate(self.stabilizers):
            if stabilizer == 1:  # If stabilizer measurement indicates an error
                error_correction.append(index)  # Record the index of the error

        if error_correction:
            return f"Errors detected at stabilizer indices: {error_correction}"
        else:
            return "No errors detected."

    def visualize(self):
        """Visualize the qubit states and stabilizers."""
        plt.imshow(self.qubits, cmap='gray', interpolation='nearest')
        plt.title('Surface Code Qubit States')
        plt.colorbar(label='Qubit State (0 or 1)')
        plt.show()

# Example usage
if __name__ == "__main__":
    surface_code = SurfaceCode(size=5)
    surface_code.apply_error(2, 2)  # Simulate an error
    stabilizers = surface_code.measure_stabilizers()
    print("Stabilizer Measurements:", stabilizers)
    print(surface_code.decode_errors())
    surface_code.visualize()

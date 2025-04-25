"""
Quantum Variational Autoencoder for Civilization Modeling.
"""
import pennylane as qml
import numpy as np

class QVAEGenerator:
    def __init__(self, n_qubits: int):
        """
        Initialize the QVAE Generator.

        Args:
            n_qubits (int): Number of qubits for the QVAE.
        """
        self.dev = qml.device("default.qubit", wires=n_qubits)
        self.n_qubits = n_qubits
        self.encoder_params = np.random.randn(n_qubits, 3) * 0.1  # Initialize small random parameters
        self.decoder_params = np.random.randn(n_qubits, 3) * 0.1

    @qml.qnode
    def encoder_circuit(self, data: np.ndarray):
        """Encode civilization data into latent space."""
        for i in range(self.n_qubits):
            qml.RX(data[i], wires=i)
            qml.Rot(*self.encoder_params[i], wires=i)
        return qml.state()

    @qml.qnode
    def decoder_circuit(self, latent: np.ndarray):
        """Decode latent space to generate civilization model."""
        for i in range(self.n_qubits):
            qml.RX(latent[i], wires=i)
            qml.Rot(*self.decoder_params[i], wires=i)
        return qml.state()

    def generate_civilization(self, data: list) -> np.ndarray:
        """Generate synthetic civilization models."""
        latent = [self.encoder_circuit(d) for d in data]
        models = [self.decoder_circuit(l) for l in latent]
        return np.array(models)

    def train(self, data: np.ndarray, epochs: int = 1000, learning_rate: float = 0.01):
        """
        Train the QVAE using the provided data.

        Args:
            data (np.ndarray): Input data for training.
            epochs (int): Number of training epochs.
            learning_rate (float): Learning rate for parameter updates.
        """
        optimizer = qml.GradientDescentOptimizer(stepsize=learning_rate)

        for epoch in range(epochs):
            loss = 0
            for d in data:
                # Forward pass
                latent = self.encoder_circuit(d)
                reconstructed = self.decoder_circuit(latent)

                # Calculate loss (Mean Squared Error)
                loss += np.mean((d - reconstructed)**2)

                # Backward pass (gradient update)
                self.encoder_params, self.decoder_params = optimizer.step(self.loss_function, self.encoder_params, self.decoder_params, d)

            loss /= len(data)
            if epoch % 100 == 0:
                print(f"Epoch {epoch}: Loss = {loss:.4f}")

    def loss_function(self, data: np.ndarray) -> float:
        """
        Calculate the loss for the given data.

        Args:
            data (np.ndarray): Input data for loss calculation.

        Returns:
            float: Loss value.
        """
        latent = self.encoder_circuit(data)
        reconstructed = self.decoder_circuit(latent)
        return np.mean((data - reconstructed)**2)

# Example usage
if __name__ == "__main__":
    n_qubits = 4
    qvae = QVAEGenerator(n_qubits)

    # Generate synthetic data for training
    synthetic_data = [np.random.rand(n_qubits) for _ in range(100)]

    # Train the QVAE
    qvae.train(np.array(synthetic_data), epochs=1000, learning_rate=0.01)

    # Generate civilization models
    models = qvae.generate_civilization(synthetic_data)
    print("Generated Civilization Models:\n", models)

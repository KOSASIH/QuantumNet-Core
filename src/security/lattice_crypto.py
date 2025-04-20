import numpy as np
import json

class LatticeCrypto:
    def __init__(self, dimension):
        self.dimension = dimension
        self.secret_key = self.generate_secret_key()

    def generate_secret_key(self):
        """Generate a random secret key based on lattice dimensions."""
        return [self.random_polynomial() for _ in range(self.dimension)]

    def random_polynomial(self):
        """Generate a random polynomial for the lattice."""
        return [np.random.randint(-1, 2) for _ in range(self.dimension)]

    def polynomial_add(self, poly1, poly2):
        """Add two polynomials."""
        return [(a + b) % 2 for a, b in zip(poly1, poly2)]

    def polynomial_multiply(self, poly1, poly2):
        """Multiply two polynomials using naive multiplication."""
        result = [0] * (2 * self.dimension - 1)
        for i in range(len(poly1)):
            for j in range(len(poly2)):
                result[i + j] += poly1[i] * poly2[j]
        return result[:self.dimension]  # Return only the relevant part

    def encrypt(self, message):
        """Encrypt a message using the secret key."""
        if len(message) != self.dimension:
            raise ValueError("Message length must match the dimension of the lattice.")
        
        noise = self.random_polynomial()  # Add some noise for security
        encrypted_message = self.polynomial_add(message, self.secret_key[0])  # Simple encryption
        encrypted_message = self.polynomial_add(encrypted_message, noise)  # Add noise
        return encrypted_message

    def decrypt(self, ciphertext):
        """Decrypt the ciphertext using the secret key."""
        if len(ciphertext) != self.dimension:
            raise ValueError("Ciphertext length must match the dimension of the lattice.")
        
        decrypted_message = self.polynomial_add(ciphertext, self.secret_key[0])  # Simple decryption
        return decrypted_message  # Return the decrypted message

    def serialize_key(self):
        """Serialize the secret key to JSON format."""
        return json.dumps(self.secret_key)

    def deserialize_key(self, key_json):
        """Deserialize the secret key from JSON format."""
        self.secret_key = json.loads(key_json)

# Example usage
if __name__ == "__main__":
    dimension = 5
    lattice_crypto = LatticeCrypto(dimension)

    # Generate a random message
    message = [np.random.randint(0, 2) for _ in range(dimension)]
    print(f"Original message: {message}")

    # Encrypt the message
    ciphertext = lattice_crypto.encrypt(message)
    print(f"Encrypted message: {ciphertext}")

    # Decrypt the message
    decrypted_message = lattice_crypto.decrypt(ciphertext)
    print(f"Decrypted message: {decrypted_message}")

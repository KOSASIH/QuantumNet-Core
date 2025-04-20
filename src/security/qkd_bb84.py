import numpy as np
import random

class BB84:
    def __init__(self):
        self.basis_a = []  # Alice's basis
        self.basis_b = []  # Bob's basis
        self.key_a = []    # Alice's key
        self.key_b = []    # Bob's key
        self.n = 0         # Number of bits

    def generate_bases(self, n):
        """Generate random bases for Alice and Bob."""
        self.n = n
        self.basis_a = np.random.choice(['+', 'x'], n)  # '+' for Z-basis, 'x' for X-basis
        self.basis_b = np.random.choice(['+', 'x'], n)

    def encode_bits(self, bits):
        """Encode bits using the chosen basis."""
        encoded_bits = []
        for bit, basis in zip(bits, self.basis_a):
            if basis == '+':
                encoded_bits.append(bit)  # 0 or 1
            else:
                encoded_bits.append(1 - bit)  # Flip the bit
        return encoded_bits

    def measure_bits(self, encoded_bits):
        """Measure the encoded bits using the chosen basis."""
        for bit, basis in zip(encoded_bits, self.basis_b):
            if basis == '+':
                self.key_b.append(bit)
            else:
                self.key_b.append(1 - bit)  # Flip the bit

    def generate_key(self, bits):
        """Generate a shared key."""
        self.generate_bases(len(bits))
        encoded_bits = self.encode_bits(bits)
        self.measure_bits(encoded_bits)
        self.key_a = bits  # Alice's key is the original bits

    def sift_keys(self):
        """Sift the keys based on the basis agreement."""
        sifted_key_a = []
        sifted_key_b = []
        for i in range(self.n):
            if self.basis_a[i] == self.basis_b[i]:
                sifted_key_a.append(self.key_a[i])
                sifted_key_b.append(self.key_b[i])
        self.key_a = sifted_key_a
        self.key_b = sifted_key_b

    def detect_eavesdropping(self, eavesdropper_rate):
        """Detect potential eavesdropping based on a predefined rate."""
        if random.random() < eavesdropper_rate:
            print("Eavesdropping detected!")
            return True
        return False

    def get_shared_key(self):
        """Return the shared key."""
        return self.key_a, self.key_b

# Example usage
if __name__ == "__main__":
    alice_bits = np.random.randint(0, 2, 10)  # Alice generates random bits
    bb84 = BB84()
    bb84.generate_key(alice_bits)
    bb84.sift_keys()

    # Simulate eavesdropping detection
    if bb84.detect_eavesdropping(0.1):  # 10% chance of eavesdropping
        print("Key exchange aborted due to eavesdropping.")
    else:
        key_a, key_b = bb84.get_shared_key()
        print(f"Alice's key: {key_a}")
        print(f"Bob's key: {key_b}")

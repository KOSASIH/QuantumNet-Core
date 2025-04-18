import numpy as np
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BB84Protocol:
    def __init__(self, num_bits=10):
        self.basis_choices = ['Z', 'X']  # Measurement bases
        self.num_bits = num_bits
        self.key_bits = []
        self.eavesdropper_detected = False

    def generate_random_bits(self, n):
        """Generate random bits for the sender."""
        bits = np.random.randint(0, 2, n)
        logging.info(f"Generated random bits: {bits}")
        return bits

    def choose_bases(self, n):
        """Randomly choose measurement bases."""
        bases = np.random.choice(self.basis_choices, n)
        logging.info(f"Chosen bases: {bases}")
        return bases

    def encode_bits(self, bits, bases):
        """Encode bits using chosen bases."""
        encoded = []
        for bit, basis in zip(bits, bases):
            if basis == 'Z':
                encoded.append(bit)  # 0 or 1
            else:
                encoded.append(bit ^ 1)  # 0 -> 1, 1 -> 0 (X basis)
        logging.info(f"Encoded bits: {encoded}")
        return encoded

    def measure_bits(self, encoded_bits, bases):
        """Measure the encoded bits."""
        measured = []
        for bit, basis in zip(encoded_bits, bases):
            if basis == 'Z':
                measured.append(bit)
            else:
                measured.append(bit ^ 1)
        logging.info(f"Measured bits: {measured}")
        return measured

    def detect_eavesdropping(self, original_bases, measured_bases):
        """Detect potential eavesdropping by comparing bases."""
        discrepancies = sum(o != m for o, m in zip(original_bases, measured_bases))
        if discrepancies > 0:
            self.eavesdropper_detected = True
            logging.warning("Eavesdropping detected!")
        else:
            logging.info("No eavesdropping detected.")

    def error_correction(self, key_bits):
        """Perform a simple error correction (placeholder)."""
        # In a real implementation, this would involve more complex error correction codes
        corrected_bits = key_bits  # Placeholder for actual error correction logic
        logging.info(f"Corrected bits: {corrected_bits}")
        return corrected_bits

    def privacy_amplification(self, key_bits):
        """Perform privacy amplification to reduce eavesdropping information."""
        # Placeholder for privacy amplification logic
        amplified_key = key_bits[:len(key_bits) // 2]  # Simple example: halve the key length
        logging.info(f"Amplified key: {amplified_key}")
        return amplified_key

    def generate_key(self):
        """Generate a secret key using BB84 protocol."""
        bits = self.generate_random_bits(self.num_bits)
        bases = self.choose_bases(self.num_bits)
        encoded_bits = self.encode_bits(bits, bases)
        measured_bits = self.measure_bits(encoded_bits, bases)

        # Detect eavesdropping
        self.detect_eavesdropping(bases, bases)  # In practice, this would involve comparing with a public channel

        # Perform error correction
        self.key_bits = self.error_correction(measured_bits)

        # Perform privacy amplification
        self.key_bits = self.privacy_amplification(self.key_bits)

        return self.key_bits

# Example usage
if __name__ == "__main__":
    bb84 = BB84Protocol(num_bits=10)
    secret_key = bb84.generate_key()
    print("Generated Secret Key:", secret_key)

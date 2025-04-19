import numpy as np
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ConcatenatedCode:
    def __init__(self, outer_code, inner_code):
        self.outer_code = outer_code
        self.inner_code = inner_code

    def encode(self, message):
        """Encode a message using concatenated codes."""
        logging.info(f"Encoding message: {message}")

        # Encode the message using the inner code
        inner_encoded = self.inner_code.encode(message)
        logging.info(f"Inner encoded message: {inner_encoded}")

        # Encode the inner encoded message using the outer code
        outer_encoded = self.outer_code.encode(inner_encoded)
        logging.info(f"Outer encoded message: {outer_encoded}")

        return outer_encoded

    def decode(self, encoded_message):
        """Decode a message using concatenated codes."""
        logging.info(f"Decoding message: {encoded_message}")

        # Decode the message using the outer code
        outer_decoded = self.outer_code.decode(encoded_message)
        logging.info(f"Outer decoded message: {outer_decoded}")

        # Decode the outer decoded message using the inner code
        inner_decoded = self.inner_code.decode(outer_decoded)
        logging.info(f"Inner decoded message: {inner_decoded}")

        return inner_decoded

# Example inner and outer code implementations for demonstration
class SimpleInnerCode:
    def encode(self, message):
        """Simple repetition code for inner encoding."""
        return ''.join([char * 3 for char in message])  # Repeat each character 3 times

    def decode(self, encoded_message):
        """Simple decoding for inner code."""
        return ''.join([encoded_message[i] for i in range(0, len(encoded_message), 3)])  # Take every third character

class SimpleOuterCode:
    def encode(self, message):
        """Simple parity check for outer encoding."""
        return message + self.calculate_parity(message)

    def decode(self, encoded_message):
        """Simple decoding for outer code."""
        message = encoded_message[:-1]  # Remove parity bit
        parity = encoded_message[-1]
        if self.check_parity(message, parity):
            return message
        else:
            logging.warning("Parity check failed!")
            return None  # Indicate an error

    def calculate_parity(self, message):
        """Calculate parity bit."""
        return '1' if message.count('1') % 2 else '0'

    def check_parity(self, message, parity):
        """Check parity bit."""
        return self.calculate_parity(message) == parity

# Example usage
if __name__ == "__main__":
    inner_code = SimpleInnerCode()
    outer_code = SimpleOuterCode()
    concatenated_code = ConcatenatedCode(outer_code=outer_code, inner_code=inner_code)

    encoded_message = concatenated_code.encode("Hello")
    print("Encoded Message:", encoded_message)

    decoded_message = concatenated_code.decode(encoded_message)
    print("Decoded Message:", decoded_message)

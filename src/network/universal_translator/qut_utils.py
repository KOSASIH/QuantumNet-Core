"""
Utility Functions for Quantum Universal Translator (QUT)
"""
import numpy as np
import re

def preprocess_text(text: str) -> str:
    """
    Preprocess the input text for translation.

    Parameters:
    text (str): The text to preprocess.

    Returns:
    str: Preprocessed text.
    """
    # Remove special characters and digits, convert to lowercase
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.strip().lower()  # Simple preprocessing

def validate_protocol(protocol: str) -> bool:
    """
    Validate the given protocol.

    Parameters:
    protocol (str): The protocol to validate.

    Returns:
    bool: True if valid, False otherwise.
    """
    # Check if the protocol is a non-empty string
    return isinstance(protocol, str) and len(protocol) > 0

def encode_protocol(protocol: str) -> np.ndarray:
    """
    Encode a protocol string into a numerical representation.

    Parameters:
    protocol (str): The protocol to encode.

    Returns:
    np.ndarray: Numerical representation of the protocol.
    """
    # Convert each character to its ASCII value and normalize
    return np.array([ord(char) / 255.0 for char in protocol], dtype=np.float32)

def decode_protocol(encoded_protocol: np.ndarray) -> str:
    """
    Decode a numerical representation back into a protocol string.

    Parameters:
    encoded_protocol (np.ndarray): The encoded protocol to decode.

    Returns:
    str: The decoded protocol string.
    """
    # Convert normalized values back to characters
    return ''.join(chr(int(value * 255)) for value in encoded_protocol)

def is_valid_protocol_mapping(protocol_mapping: dict) -> bool:
    """
    Validate the structure of a protocol mapping.

    Parameters:
    protocol_mapping (dict): The protocol mapping to validate.

    Returns:
    bool: True if valid, False otherwise.
    """
    if not isinstance(protocol_mapping, dict):
        return False
    for key, value in protocol_mapping.items():
        if not validate_protocol(key) or not validate_protocol(value):
            return False
    return True

# Example usage:
if __name__ == "__main__":
    # Test preprocessing
    raw_text = "  Hello, World! 123 "
    processed_text = preprocess_text(raw_text)
    print("Processed Text:", processed_text)

    # Test protocol validation
    protocol = "quantum_teleportation"
    print("Is valid protocol:", validate_protocol(protocol))

    # Test encoding and decoding
    encoded = encode_protocol(protocol)
    print("Encoded Protocol:", encoded)
    decoded = decode_protocol(encoded)
    print("Decoded Protocol:", decoded)

    # Test protocol mapping validation
    mapping = {
        "quantum_teleportation": "universal_representation_1",
        "quantum_key_distribution": "universal_representation_2"
    }
    print("Is valid mapping:", is_valid_protocol_mapping(mapping))

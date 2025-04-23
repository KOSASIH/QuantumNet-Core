### `test_error_correction.py`

import unittest

class ErrorCorrection:
    """A simple error correction class using Hamming code for demonstration."""
    
    def encode(self, data):
        """Encode data using Hamming(7,4) code."""
        # Assuming data is a 4-bit string
        if len(data) != 4 or not all(bit in '01' for bit in data):
            raise ValueError("Input must be a 4-bit binary string.")
        
        # Hamming(7,4) encoding
        p1 = int(data[0]) ^ int(data[1]) ^ int(data[3])  # parity bit 1
        p2 = int(data[0]) ^ int(data[2]) ^ int(data[3])  # parity bit 2
        p3 = int(data[1]) ^ int(data[2]) ^ int(data[3])  # parity bit 3
        
        return f"{p1}{p2}{data[0]}{p3}{data[1]}{data[2]}{data[3]}"

    def decode(self, encoded):
        """Decode Hamming(7,4) encoded data and correct single-bit errors."""
        if len(encoded) != 7 or not all(bit in '01' for bit in encoded):
            raise ValueError("Input must be a 7-bit binary string.")
        
        # Extract bits
        p1, p2, d1, p3, d2, d3, d4 = map(int, encoded)
        
        # Calculate parity
        s1 = p1 ^ d1 ^ d2 ^ d4
        s2 = p2 ^ d1 ^ d3 ^ d4
        s3 = p3 ^ d2 ^ d3 ^ d4
        
        # Error position
        error_position = s1 * 1 + s2 * 2 + s3 * 4
        
        if error_position:
            # Correct the error
            encoded = list(encoded)
            encoded[error_position - 1] = '1' if encoded[error_position - 1] == '0' else '0'
            encoded = ''.join(encoded)
        
        # Return the corrected data
        return encoded[2:5]  # Return the original 4 data bits

class TestErrorCorrection(unittest.TestCase):

    def setUp(self):
        """Set up the error correction instance."""
        self.ec = ErrorCorrection()

    def test_encoding(self):
        """Test encoding of 4-bit data."""
        encoded = self.ec.encode("1011")
        self.assertEqual(encoded, "1101011")  # Expected Hamming(7,4) code

    def test_decoding(self):
        """Test decoding of encoded data."""
        decoded = self.ec.decode("1101011")
        self.assertEqual(decoded, "1011")  # Should return original data

    def test_single_bit_error_correction(self):
        """Test correction of a single-bit error."""
        corrected = self.ec.decode("1101001")  # Simulate a single-bit error
        self.assertEqual(corrected, "1011")  # Should correct to original data

    def test_invalid_encoding_input(self):
        """Test error handling for invalid encoding input."""
        with self.assertRaises(ValueError):
            self.ec.encode("101")  # Not a 4-bit string
        with self.assertRaises(ValueError):
            self.ec.encode("1020")  # Invalid binary string

    def test_invalid_decoding_input(self):
        """Test error handling for invalid decoding input."""
        with self.assertRaises(ValueError):
            self.ec.decode("11010")  # Not a 7-bit string
        with self.assertRaises(ValueError):
            self.ec.decode("1101002")  # Invalid binary string

if __name__ == '__main__':
    unittest.main()

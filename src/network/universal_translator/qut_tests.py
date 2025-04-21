import unittest
import numpy as np
from universal_translator.qnlp_translator import QNLTranslator
from universal_translator.protocol_mapper import ProtocolMapper
from universal_translator.qut_utils import preprocess_text, validate_protocol, encode_protocol, decode_protocol

class TestQNLTranslator(unittest.TestCase):
    def setUp(self):
        """Set up the QNLP translator for testing."""
        self.translator = QNLTranslator(n_qubits=3)

    def test_translate(self):
        """Test the translation functionality."""
        input_text = "Hello"
        translated_text = self.translator.translate(input_text)
        self.assertEqual(translated_text, "olleh")  # Check if the text is reversed (placeholder logic)

    def test_encode_to_quantum(self):
        """Test encoding text to a quantum circuit."""
        input_text = "A"
        circuit = self.translator.encode_to_quantum(input_text)
        self.assertEqual(circuit.num_qubits, 3)  # Check if the circuit has the correct number of qubits

    def test_decode_from_quantum(self):
        """Test decoding from a quantum circuit."""
        circuit = self.translator.encode_to_quantum("A")
        decoded_text = self.translator.decode_from_quantum(circuit)
        self.assertEqual(decoded_text, "Decoded Text")  # Check placeholder return

    def test_train(self):
        """Test the training functionality of the translator."""
        protocol_pairs = [
            (np.array([0.1, 0.2, 0.3]), np.array([0.9, 0.8, 0.7])),
            (np.array([0.4, 0.5, 0.6]), np.array([0.6, 0.5, 0.4])),
        ]
        self.translator.train(protocol_pairs, epochs=10)  # Ensure no exceptions are raised

class TestProtocolMapper(unittest.TestCase):
    def setUp(self):
        """Set up the protocol mapper for testing."""
        self.mapper = ProtocolMapper('protocols.json')  # Assuming a protocols.json file exists

    def test_map_protocol(self):
        """Test mapping a protocol to its universal representation."""
        result = self.mapper.map_protocol("example_protocol")
        self.assertNotEqual(result, "Unknown Protocol")  # Check if the protocol is recognized

    def test_add_protocol(self):
        """Test adding a new protocol."""
        new_protocol = "new_protocol"
        universal_representation = "universal_representation_for_new_protocol"
        self.mapper.add_protocol(new_protocol, universal_representation)
        self.assertEqual(self.mapper.map_protocol(new_protocol), universal_representation)

    def test_save_protocols(self):
        """Test saving protocols to a file."""
        self.mapper.save_protocols('test_protocols.json')  # Save to a test file
        with open('test_protocols.json', 'r') as file:
            protocols = json.load(file)
            self.assertIn("new_protocol", protocols)  # Check if the new protocol is saved

class TestQUTUtils(unittest.TestCase):
    def test_preprocess_text(self):
        """Test text preprocessing."""
        raw_text = "  Hello World  "
        processed_text = preprocess_text(raw_text)
        self.assertEqual(processed_text, "hello world")  # Check if text is stripped and lowercased

    def test_validate_protocol(self):
        """Test protocol validation."""
        valid_protocol = "quantum_teleportation"
        invalid_protocol = ""
        self.assertTrue(validate_protocol(valid_protocol))  # Check valid protocol
        self.assertFalse(validate_protocol(invalid_protocol))  # Check invalid protocol

    def test_encode_protocol(self):
        """Test encoding a protocol."""
        protocol = "quantum_teleportation"
        encoded = encode_protocol(protocol)
        self.assertEqual(len(encoded), len(protocol))  # Check if encoded length matches

    def test_decode_protocol(self):
        """Test decoding a protocol."""
        protocol = "quantum_teleportation"
        encoded = encode_protocol(protocol)
        decoded = decode_protocol(encoded)
        self.assertEqual(decoded, protocol)  # Check if decoded matches original

if __name__ == "__main__":
    unittest.main()

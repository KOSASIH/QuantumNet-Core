import unittest
from unittest.mock import patch
from .threat_detector import ThreatDetector
from .response_engine import ResponseEngine
from .qtdr_utils import log_event, validate_data, sanitize_input

class TestThreatDetector(unittest.TestCase):
    def setUp(self):
        self.detector = ThreatDetector()

    def test_detect_quantum_attack(self):
        result = self.detector.detect_threat("This is a quantum_attack test.")
        self.assertTrue(result)
        self.assertIn({"type": "Quantum Attack", "message": "Quantum attack detected!"}, self.detector.get_threats())

    def test_detect_data_breach(self):
        result = self.detector.detect_threat("This is a data_breach test.")
        self.assertTrue(result)
        self.assertIn({"type": "Data Breach", "message": "Data breach detected!"}, self.detector.get_threats())

    def test_detect_anomaly(self):
        # Simulate anomaly detection
        self.detector.data_history = [[1, 2], [2, 3], [3, 4]]  # Mock historical data
        result = self.detector.detect_threat([10, 10])  # Anomalous data
        self.assertTrue(result)
        self.assertIn({"type": "Anomaly", "message": "Anomalous behavior detected!"}, self.detector.get_threats())

    def test_no_threat(self):
        result = self.detector.detect_threat("This is a safe message.")
        self.assertFalse(result)
        self.assertEqual(self.detector.get_threats(), [])

class TestResponseEngine(unittest.TestCase):
    def setUp(self):
        self.engine = ResponseEngine(notification_email='admin@example.com')

    def test_respond_to_quantum_attack(self):
        threat = {"type": "Quantum Attack", "message": "Quantum attack detected!"}
        with patch('src.security.qtdr.response_engine.smtplib.SMTP') as mock_smtp:
            self.engine.respond_to_threat(threat)
            self.assertIn("Initiating countermeasures for: Quantum attack detected!", self.engine.get_responses())
            mock_smtp.assert_called_once()  # Check if notification was sent

    def test_respond_to_data_breach(self):
        threat = {"type": "Data Breach", "message": "Unauthorized access detected!"}
        self.engine.respond_to_threat(threat)
        self.assertIn("Data breach detected! Initiating lockdown procedures.", self.engine.get_responses())

    def test_respond_to_anomaly(self):
        threat = {"type": "Anomaly", "message": "Unusual login activity detected."}
        self.engine.respond_to_threat(threat)
        self.assertIn("Anomaly detected: Unusual login activity detected. Investigating...", self.engine.get_responses())

class TestUtils(unittest.TestCase):
    def test_log_event(self):
        with patch('src.security.qtdr.qtdr_utils.logging.info') as mock_log:
            log_event("Test event logged.")
            mock_log.assert_called_once_with("Security Event: Test event logged.")

    def test_validate_data(self):
        self.assertTrue(validate_data("Valid data"))
        with self.assertRaises(ValueError):
            validate_data(123)  # Invalid data type
        with self.assertRaises(ValueError):
            validate_data("Too long" * 20)  # Exceeds max length

    def test_sanitize_input(self):
        sanitized = sanitize_input("<script>alert('XSS');</script>")
        self.assertEqual(sanitized, "scriptalert('XSS');/script")  # Check for angle brackets removal
        self.assertEqual(sanitize_input("Safe input"), "Safe input")  # No change for safe input

if __name__ == "__main__":
    unittest.main()

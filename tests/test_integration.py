# tests/test_integration.py

import unittest
from integration.qiskit_integration import QiskitIntegration
from integration.cirq_integration import CirqIntegration

class TestIntegration(unittest.TestCase):

    def test_qiskit_integration(self):
        """Test Qiskit integration functionality."""
        qiskit_backend = QiskitIntegration()
        circuit = qiskit_backend.create_circuit(2)
        self.assertIsNotNone(circuit)

    def test_cirq_integration(self):
        """Test Cirq integration functionality."""
        cirq_backend = CirqIntegration()
        circuit = cirq_backend.create_circuit(2)
        self.assertIsNotNone(circuit)

if __name__ == "__main__":
    unittest.main()

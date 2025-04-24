"""
Unit tests for the Autonomous Quantum Diplomacy Engine (AQDE).
This module tests the functionality and performance of the AQDE.
"""

import unittest
from diplomacy_engine import AutonomousQuantumDiplomacyEngine  # Assuming AQDE is implemented in diplomacy_engine.py

class TestAutonomousQuantumDiplomacyEngine(unittest.TestCase):
    def setUp(self):
        """Set up the test environment for AQDE."""
        self.engine = AutonomousQuantumDiplomacyEngine()

    def test_initialization(self):
        """Test the initialization of the AQDE."""
        self.assertIsNotNone(self.engine)
        self.assertEqual(self.engine.current_state, "idle")  # Assuming default state is idle
        self.assertIsInstance(self.engine.negotiation_history, list)
        self.assertEqual(len(self.engine.negotiation_history), 0)

    def test_initiate_negotiation(self):
        """Test the initiation of a negotiation."""
        self.engine.initiate_negotiation("Country A", "Country B")
        self.assertEqual(self.engine.current_state, "negotiating")
        self.assertIn(("Country A", "Country B"), self.engine.negotiation_history)

    def test_decision_making(self):
        """Test the decision-making process of the AQDE."""
        self.engine.initiate_negotiation("Country A", "Country B")
        decision = self.engine.make_decision()
        self.assertIn(decision, ["agree", "disagree", "compromise"])  # Assuming these are possible decisions

    def test_performance_metrics(self):
        """Test the performance metrics of the AQDE."""
        self.engine.initiate_negotiation("Country A", "Country B")
        metrics = self.engine.calculate_performance_metrics()
        self.assertIn('negotiation_time', metrics)
        self.assertIn('success_rate', metrics)
        self.assertGreater(metrics['negotiation_time'], 0)
        self.assertGreaterEqual(metrics['success_rate'], 0)  # Success rate should be non-negative

    def test_error_handling(self):
        """Test error handling for invalid operations."""
        with self.assertRaises(RuntimeError):
            self.engine.make_decision()  # Should raise an error if no negotiation is active

        self.engine.initiate_negotiation("Country A", "Country B")  # Start negotiation
        self.engine.make_decision()  # Valid decision making should not raise an error

    def test_edge_cases(self):
        """Test edge cases for the AQDE."""
        # Test initiating negotiation with the same country
        with self.assertRaises(ValueError):
            self.engine.initiate_negotiation("Country A", "Country A")  # Should raise an error

        # Test negotiation with multiple countries
        self.engine.initiate_negotiation("Country A", "Country B")
        self.engine.initiate_negotiation("Country C", "Country D")
        self.assertEqual(len(self.engine.negotiation_history), 2)  # Should have two negotiations

if __name__ == "__main__":
    unittest.main()

import unittest
import numpy as np
from qrc_emulator import QRCEmulator
from crisis_simulator import CrisisSimulator
from qce_utils import generate_crisis_data, analyze_state, normalize_state

class TestQRCEmulator(unittest.TestCase):
    def setUp(self):
        self.emulator = QRCEmulator(n_qubits=5)

    def test_initial_state(self):
        """Test that the initial state has the correct number of qubits."""
        state = self.emulator.get_state()
        self.assertEqual(len(state), 5)

    def test_update_state(self):
        """Test that the state updates correctly with new inputs."""
        initial_state = self.emulator.get_state()
        inputs = np.random.rand(5)
        self.emulator.update_state(inputs)
        updated_state = self.emulator.get_state()
        self.assertFalse(np.array_equal(initial_state, updated_state))

    def test_reset(self):
        """Test that the state resets correctly."""
        self.emulator.reset()
        state_after_reset = self.emulator.get_state()
        self.assertEqual(len(state_after_reset), 5)

    def test_training(self):
        """Test the training process of the QRC emulator."""
        crisis_data = [
            (np.array([0.1, 0.2, 0.3, 0.4, 0.5]), np.array([0.5, 0.6, 0.7, 0.8, 0.9])),
            (np.array([0.2, 0.3, 0.4, 0.5, 0.6]), np.array([0.6, 0.7, 0.8, 0.9, 1.0])),
        ]
        self.emulator.train(crisis_data, epochs=10)
        # Check if parameters have been updated (not all zeros)
        self.assertTrue(np.any(self.emulator.params != 0))

    def test_prediction(self):
        """Test the prediction capability of the QRC emulator."""
        inputs = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
        self.emulator.train([(inputs, np.array([0.5, 0.6, 0.7, 0.8, 0.9]))], epochs=10)
        prediction = self.emulator.predict(inputs)
        self.assertEqual(len(prediction), 5)

class TestCrisisSimulator(unittest.TestCase):
    def setUp(self):
        self.emulator = QRCEmulator(n_qubits=5)
        self.simulator = CrisisSimulator(self.emulator)

    def test_simulate_crisis(self):
        """Test that simulating a crisis updates the state correctly."""
        crisis_data = np.random.rand(5)
        updated_state = self.simulator.simulate_crisis(crisis_data)
        self.assertEqual(len(updated_state), 5)

    def test_run_multiple_crises(self):
        """Test running multiple crisis scenarios."""
        crisis_scenarios = [np.random.rand(5) for _ in range(3)]
        updated_states = self.simulator.run_multiple_crises(crisis_scenarios)
        self.assertEqual(len(updated_states), 3)
        for state in updated_states:
            self.assertEqual(len(state), 5)

    def test_analyze_crisis_impact(self):
        """Test the analysis of crisis impact on the consciousness state."""
        crisis_data = np.random.rand(5)
        analysis = self.simulator.analyze_crisis_impact(crisis_data)
        self.assertIn('mean', analysis)
        self.assertIn('variance', analysis)
        self.assertIn('max', analysis)
        self.assertIn('min', analysis)

if __name__ == '__main__':
    unittest.main()

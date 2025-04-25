import unittest
import numpy as np
from src.entanglement.temporal.qtep_utils import QTEPUtils
from src.entanglement.temporal.qtep_visualization import QTEPVisualization

class TestQTEPUtils(unittest.TestCase):

    def test_prepare_initial_state_random(self):
        num_qubits = 3
        state = QTEPUtils.prepare_initial_state(num_qubits, 'random')
        self.assertEqual(len(state), num_qubits)
        self.assertTrue(np.all(np.isin(state, [0, 1])))

    def test_prepare_initial_state_zero(self):
        num_qubits = 3
        state = QTEPUtils.prepare_initial_state(num_qubits, 'zero')
        self.assertTrue(np.all(state == 0))

    def test_apply_noise(self):
        state = np.array([1, 0, 0, 0])
        noisy_state = QTEPUtils.apply_noise(state, 0.1)
        self.assertEqual(len(noisy_state), len(state))
        self.assertTrue(np.any(noisy_state != state) or np.array_equal(noisy_state, state))

    def test_measure_state(self):
        state = np.array([1, 0, 0, 0])  # |0> state
        measurement = QTEPUtils.measure_state(state)
        self.assertEqual(measurement, 0)

    def test_convert_to_density_matrix(self):
        state = np.array([1, 0, 0, 0])  # |0> state
        density_matrix = QTEPUtils.convert_to_density_matrix(state)
        expected_density_matrix = np.array([[1, 0, 0, 0],
                                             [0, 0, 0, 0],
                                             [0, 0, 0, 0],
                                             [0, 0, 0, 0]])
        np.testing.assert_array_equal(density_matrix, expected_density_matrix)

class TestQTEPVisualization(unittest.TestCase):

    def test_plot_probability_distribution(self):
        state = np.array([1, 0, 0, 0])  # |0> state
        try:
            QTEPVisualization.plot_probability_distribution(state)
        except Exception as e:
            self.fail(f"plot_probability_distribution raised an exception: {e}")

    def test_plot_state_evolution(self):
        states = np.array([[1, 0, 0, 0], [0, 1, 0, 0]])  # |0> and |1> states
        try:
            QTEPVisualization.plot_state_evolution(states)
        except Exception as e:
            self.fail(f"plot_state_evolution raised an exception: {e}")

    def test_plot_density_matrix(self):
        state = np.array([1, 0, 0, 0])  # |0> state
        density_matrix = QTEPUtils.convert_to_density_matrix(state)
        try:
            QTEPVisualization.plot_density_matrix(density_matrix)
        except Exception as e:
            self.fail(f"plot_density_matrix raised an exception: {e}")

    def test_plot_measurement_results(self):
        results = [0, 1, 0, 1, 0]  # Example measurement results
        try:
            QTEPVisualization.plot_measurement_results(results)
        except Exception as e:
            self.fail(f"plot_measurement_results raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()

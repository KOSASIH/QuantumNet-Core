import unittest
import numpy as np
from resource_optimizer.qbo_optimizer import QBOOptimizer
from resource_optimizer.resource_predictor import ResourcePredictor
from resource_optimizer.qrho_utils import (
    normalize_resource_allocation,
    calculate_resource_efficiency,
    calculate_resource_shortfall,
    calculate_resource_surplus,
    aggregate_resource_allocations
)

class TestQBOOptimizer(unittest.TestCase):
    def setUp(self):
        self.resource_limits = {'qubits': 10, 'gates': 50}
        self.optimizer = QBOOptimizer(n_qubits=len(self.resource_limits))

    def test_optimize_resources_within_limits(self):
        demand = {'qubits': 8, 'gates': 40}
        allocation = self.optimizer.optimize(demand)
        self.assertEqual(allocation['qubits'], 8)
        self.assertEqual(allocation['gates'], 40)

    def test_optimize_resources_exceeding_limits(self):
        demand = {'qubits': 12, 'gates': 60}
        allocation = self.optimizer.optimize(demand)
        self.assertEqual(allocation['qubits'], 10)  # Limited by resource limits
        self.assertEqual(allocation['gates'], 50)   # Limited by resource limits

    def test_get_current_allocation(self):
        demand = {'qubits': 5, 'gates': 30}
        self.optimizer.optimize(demand)
        current_allocation = self.optimizer.get_current_allocation()
        self.assertEqual(current_allocation['qubits'], 5)
        self.assertEqual(current_allocation['gates'], 30)

class TestResourcePredictor(unittest.TestCase):
    def setUp(self):
        self.predictor = ResourcePredictor()
        self.historical_data = np.array([[1, 2], [2, 3], [3, 4]])
        self.resource_usage = np.array([1, 2, 3])
        self.predictor.train(self.historical_data, self.resource_usage)

    def test_predict(self):
        new_data = np.array([[4, 5]])
        prediction = self.predictor.predict(new_data)
        self.assertAlmostEqual(prediction[0], 4)  # Based on linear regression

    def test_predict_untrained_model(self):
        untrained_predictor = ResourcePredictor()
        new_data = np.array([[4, 5]])
        with self.assertRaises(RuntimeError):
            untrained_predictor.predict(new_data)

class TestQRHOUtils(unittest.TestCase):
    def test_normalize_resource_allocation(self):
        allocation = {'qubits': 2, 'gates': 3}
        normalized = normalize_resource_allocation(allocation)
        self.assertAlmostEqual(sum(normalized.values()), 1.0)

    def test_calculate_resource_efficiency(self):
        allocation = {'qubits': 5, 'gates': 10}
        demand = {'qubits': 10, 'gates': 20}
        efficiency = calculate_resource_efficiency(allocation, demand)
        self.assertAlmostEqual(efficiency, 0.5)

    def test_calculate_resource_shortfall(self):
        allocation = {'qubits': 5, 'gates': 10}
        demand = {'qubits': 10, 'gates': 20}
        shortfall = calculate_resource_shortfall(allocation, demand)
        self.assertEqual(shortfall['qubits'], 5)
        self.assertEqual(shortfall['gates'], 10)

    def test_calculate_resource_surplus(self):
        allocation = {'qubits': 15, 'gates': 30}
        demand = {'qubits': 10, 'gates': 20}
        surplus = calculate_resource_surplus(allocation, demand)
        self.assertEqual(surplus['qubits'], 5)
        self.assertEqual(surplus['gates'], 10)

    def test_aggregate_resource_allocations(self):
        allocations = [{'qubits': 3, 'gates': 5}, {'qubits': 2, 'gates': 4}]
        aggregated_allocation = aggregate_resource_allocations(allocations)
        self.assertEqual(aggregated_allocation['qubits'], 5)
        self.assertEqual(aggregated_allocation['gates'], 9)

if __name__ == '__main__':
    unittest.main()

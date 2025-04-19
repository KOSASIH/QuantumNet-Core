import unittest
from unittest.mock import patch
from .qaoa_allocator import QAOAAllocator
from .resource_monitor import ResourceMonitor
from .allocator_utils import generate_random_resources, calculate_utilization, round_robin_allocation, weighted_allocation

class TestQAOAllocator(unittest.TestCase):
    def setUp(self):
        self.num_resources = 3
        self.cost_function = lambda i, j: (i + j) % 2 == 0  # Example cost function
        self.allocator = QAOAAllocator(num_resources=self.num_resources, cost_function=self.cost_function)

    def test_allocate_resources(self):
        """Test resource allocation using QAOA."""
        p = 2  # Number of layers
        optimal_allocation, counts = self.allocator.allocate_resources(p)
        self.assertIsNotNone(optimal_allocation)
        self.assertIsInstance(counts, dict)

    def test_create_qaoa_circuit(self):
        """Test the creation of the QAOA circuit."""
        p = 2
        circuit = self.allocator.create_qaoa_circuit(p)
        self.assertEqual(circuit.num_qubits, self.num_resources)

    def test_add_cost_layer(self):
        """Test the addition of cost layers to the QAOA circuit."""
        circuit = self.allocator.create_qaoa_circuit(1)
        self.allocator.add_cost_layer(circuit, 0)
        # Check if the circuit has the expected gates (this is a placeholder)
        self.assertGreater(len(circuit.data), 0)

    def test_process_results(self):
        """Test the processing of results from the QAOA execution."""
        mock_result = {'00': 5, '01': 3, '10': 2}
        with patch('qiskit.result.Result.get_counts', return_value=mock_result):
            optimal_allocation, counts = self.allocator.process_results(mock_result)
            self.assertEqual(optimal_allocation, '00')

class TestResourceMonitor(unittest.TestCase):
    def setUp(self):
        self.monitor = ResourceMonitor()

    def test_update_resources(self):
        """Test updating resources for a node."""
        self.monitor.update_resources("Node1", {"CPU": 70, "Memory": 50})
        self.assertIn("Node1", self.monitor.resources)

    def test_get_resource_status(self):
        """Test getting resource status for a node."""
        self.monitor.update_resources("Node1", {"CPU": 70, "Memory": 50})
        status = self.monitor.get_resource_status("Node1")
        self.assertEqual(status, {"CPU": 70, "Memory": 50})

    def test_check_resource_utilization(self):
        """Test checking resource utilization against thresholds."""
        self.monitor.update_resources("Node1", {"CPU": 90, "Memory": 60})
        thresholds = {"CPU": 80, "Memory": 70}
        self.monitor.check_resource_utilization("Node1", thresholds)
        alerts = self.monitor.get_alerts()
        self.assertGreater(len(alerts), 0)

class TestAllocatorUtils(unittest.TestCase):
    def test_generate_random_resources(self):
        """Test generating random resources."""
        resources = generate_random_resources(5, resource_types=['CPU', 'Memory'], distribution='uniform')
        self.assertEqual(len(resources), 2)
        self.assertIn('CPU', resources)
        self.assertIn('Memory', resources)

    def test_calculate_utilization(self):
        """Test calculating utilization metrics."""
        resources = {'CPU': 70, 'Memory': 50}
        metrics = calculate_utilization(resources)
        self.assertEqual(metrics['total'], 120)
        self.assertEqual(metrics['average'], 60)

    def test_round_robin_allocation(self):
        """Test round-robin allocation of resources."""
        resources = {'CPU': 100, 'Memory': 200}
        allocations = round_robin_allocation(resources, 5)
        self.assertEqual(len(allocations), 5)

    def test_weighted_allocation(self):
        """Test weighted allocation of resources."""
        resources = {'CPU': 100, ' Memory': 200}
        weights = {'CPU': 0.5, 'Memory': 0.5}
        allocations = weighted_allocation(resources, weights)
        self.assertEqual(len(allocations), 2)
        self.assertAlmostEqual(allocations[0][1], 50)  # 100 * 0.5
        self.assertAlmostEqual(allocations[1][1], 100)  # 200 * 0.5

    def test_invalid_distribution(self):
        """Test error handling for invalid distribution type."""
        with self.assertRaises(ValueError):
            generate_random_resources(5, distribution='invalid')

    def test_empty_resource_utilization(self):
        """Test utilization calculation with empty resources."""
        metrics = calculate_utilization({})
        self.assertEqual(metrics['total'], 0)
        self.assertEqual(metrics['average'], 0)
        self.assertEqual(metrics['max'], 0)
        self.assertEqual(metrics['min'], 0)

if __name__ == "__main__":
    unittest.main()

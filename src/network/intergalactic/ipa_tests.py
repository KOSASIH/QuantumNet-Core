import unittest
import json
from ipa_utils import (
    load_protocols,
    adapt_protocol,
    calculate_performance_metrics,
    process_data,
    save_results
)

class TestIPAUtils(unittest.TestCase):
    def setUp(self):
        """Set up test variables."""
        self.protocols = [
            {
                'id': 'protocol_1',
                'protocol': {'timeout': 100, 'max_retries': 3},
                'results': {'success': 80, 'failure': 20}
            },
            {
                'id': 'protocol_2',
                'protocol': {'timeout': 200, 'max_retries': 5},
                'results': {'success': 50, 'failure': 50}
            }
        ]
        self.adaptation_rules = {'timeout': 300, 'max_retries': 5}

    def test_load_protocols(self):
        """Test loading protocols from a JSON file."""
        with open('test_protocols.json', 'w') as f:
            json.dump(self.protocols, f)

        loaded_protocols = load_protocols('test_protocols.json')
        self.assertEqual(len(loaded_protocols), 2)
        self.assertEqual(loaded_protocols[0]['id'], 'protocol_1')

    def test_adapt_protocol(self):
        """Test adapting a protocol with given rules."""
        adapted_protocol = adapt_protocol(self.protocols[0]['protocol'], self.adaptation_rules)
        self.assertEqual(adapted_protocol['timeout'], 300)
        self.assertEqual(adapted_protocol['max_retries'], 5)

    def test_calculate_performance_metrics(self):
        """Test performance metrics calculation."""
        results = {'success': 80, 'failure': 20}
        metrics = calculate_performance_metrics(results)
        self.assertAlmostEqual(metrics['success_rate'], 0.8)
        self.assertAlmostEqual(metrics['failure_rate'], 0.2)
        self.assertEqual(metrics['total_shots'], 100)

    def test_process_data(self):
        """Test processing of raw data."""
        processed_data = process_data(self.protocols)
        self.assertEqual(len(processed_data), 2)
        self.assertEqual(processed_data[0]['protocol_id'], 'protocol_1')
        self.assertEqual(processed_data[0]['adapted']['timeout'], 300)

    def test_save_results(self):
        """Test saving results to a JSON file."""
        results_to_save = [{'id': 'protocol_1', 'metrics': {'success_rate': 0.8}}]
        save_results(results_to_save, 'test_results.json')

        with open('test_results.json', 'r') as f:
            saved_results = json.load(f)
        self.assertEqual(len(saved_results), 1)
        self.assertEqual(saved_results[0]['id'], 'protocol_1')

if __name__ == '__main__':
    unittest.main()

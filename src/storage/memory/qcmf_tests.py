"""
Unit Tests for Quantum Cosmic Memory Fabric (QCMF).
"""
import unittest
import numpy as np
from storage.memory.holographic_memory import HolographicMemory
from storage.memory.quantum_ledger import QuantumLedger
from storage.memory.memory_simulator import MemorySimulator
from storage.memory.qcmf_utils import (
    generate_random_state,
    validate_state,
    normalize_state,
    encode_classical_data,
    decode_quantum_state,
    calculate_inner_product,
    measure_state
)
from storage.memory.qcmf_visualization import plot_memory_distribution

class TestHolographicMemory(unittest.TestCase):
    def test_store_and_retrieve(self):
        memory = HolographicMemory(n_qubits=2)
        state = np.array([1, 0, 0, 0])  # |00>
        memory.store_state(state)
        retrieved_state = memory.retrieve_state(0)
        np.testing.assert_array_equal(retrieved_state, state)

    def test_distribute_ledger(self):
        memory = HolographicMemory(n_qubits=2)
        state = np.array([1, 0, 0, 0])  # |00>
        memory.store_state(state)
        nodes = ['Node1', 'Node2']
        distributed_memory = memory.distribute_ledger(nodes)
        self.assertEqual(len(distributed_memory), len(nodes))

class TestQuantumLedger(unittest.TestCase):
    def test_create_block(self):
        ledger = QuantumLedger()
        transactions = [{'from': 'Alice', 'to': 'Bob', 'amount': 10}]
        new_block = ledger.create_block(transactions)
        self.assertIn('hash', new_block)
        self.assertEqual(len(ledger.blocks), 1)

    def test_verify_block(self):
        ledger = QuantumLedger()
        transactions = [{'from': 'Alice', 'to': 'Bob', 'amount': 10}]
        new_block = ledger.create_block(transactions)
        is_valid = ledger.verify_block(new_block)
        self.assertTrue(is_valid)

class TestMemorySimulator(unittest.TestCase):
    def test_allocate_and_retrieve_memory(self):
        simulator = MemorySimulator(size=1024)
        data_to_store = b'Hello'
        simulator.allocate_memory(address=0, data=data_to_store)
        retrieved_data = simulator.retrieve_memory(address=0, length=len(data_to_store))
        self.assertEqual(retrieved_data, data_to_store)

    def test_clear_memory(self):
        simulator = MemorySimulator(size=1024)
        data_to_store = b'Hello'
        simulator.allocate_memory(address=0, data=data_to_store)
        simulator.clear_memory()
        retrieved_data = simulator.retrieve_memory(address=0, length=len(data_to_store))
        self.assertEqual(retrieved_data, b'\x00\x00\x00\x00\x00')  # Should be cleared

class TestQCMFUtils(unittest.TestCase):
    def test_generate_random_state(self):
        state = generate_random_state(n_qubits=2)
        self.assertEqual(state.shape[0], 4)  # 2 qubits -> 4 basis states

    def test_validate_state(self):
        valid_state = np.array([1, 0, 0, 0])
        self.assertTrue(validate_state(valid_state))

    def test_normalize_state(self):
        state = np.array([1, 1])
        normalized_state = normalize_state(state)
        self.assertAlmostEqual(np.linalg.norm(normalized_state), 1.0)

    def test_encode_and_decode_classical_data(self):
        classical_data = [1, 0, 0, 1]
        encoded_state = encode_classical_data(classical_data)
        decoded_data = decode_quantum_state(encoded_state)
        self.assertEqual(decoded_data, classical_data)

    def test_calculate_inner_product(self):
        state1 = np.array([1, 0])
        state2 = np.array([0, 1])
        inner_product = calculate_inner_product(state1, state2)
        self.assertEqual(inner_product, 0)

    def test_measure_state(self):
        state = np.array([1, 0])  # |0>
        measurement_result = measure_state(state)
        self.assertEqual(measurement_result, 0)

# Run the tests
if __name__ == "__main__":
    unittest.main()

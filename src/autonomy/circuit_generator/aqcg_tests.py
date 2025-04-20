import unittest
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from circuit_dataset import CircuitDataset
from circuit_evaluator import CircuitEvaluator
from aqcg_utils import (
    visualize_circuit,
    plot_histogram_data,
    plot_state_vector,
    circuit_to_matrix,
    matrix_to_circuit,
    random_unitary,
    fidelity,
    normalize_vector
)

class TestCircuitDataset(unittest.TestCase):
    def setUp(self):
        self.dataset = CircuitDataset()
        self.circuit = QuantumCircuit(2)
        self.circuit.h(0)
        self.circuit.cx(0, 1)
        self.dataset.add_circuit(self.circuit)

    def test_load_save_dataset(self):
        self.dataset.save_dataset('test_dataset.json')
        new_dataset = CircuitDataset('test_dataset.json')
        self.assertEqual(len(new_dataset.dataset), 1)

    def test_add_circuit(self):
        initial_size = len(self.dataset.dataset)
        new_circuit = QuantumCircuit(2)
        new_circuit.h(1)
        self.dataset.add_circuit(new_circuit)
        self.assertEqual(len(self.dataset.dataset), initial_size + 1)

    def test_split_dataset(self):
        self.dataset.add_circuit(self.circuit)
        train_set, test_set = self.dataset.split_dataset(0.5)
        self.assertEqual(len(train_set), 1)
        self.assertEqual(len(test_set), 1)

class TestCircuitEvaluator(unittest.TestCase):
    def setUp(self):
        self.evaluator = CircuitEvaluator()
        self.circuit1 = QuantumCircuit(2)
        self.circuit1.h(0)
        self.circuit1.cx(0, 1)
        self.circuit2 = QuantumCircuit(2)
        self.circuit2.h(0)
        self.circuit2.cx(0, 1)

    def test_fidelity(self):
        fidelity_value = self.evaluator.calculate_fidelity(self.circuit1, self.circuit2)
        self.assertAlmostEqual(fidelity_value, 1.0)

    def test_gate_count(self):
        gate_count = self.evaluator.count_gates(self.circuit1)
        self.assertEqual(gate_count, 2)

    def test_execute_circuit(self):
        counts, execution_time = self.evaluator.execute_circuit(self.circuit1, shots=1024)
        self.assertIsInstance(counts, dict)
        self.assertGreater(execution_time, 0)

class TestAQCGUtils(unittest.TestCase):
    def setUp(self):
        self.circuit = QuantumCircuit(2)
        self.circuit.h(0)
        self.circuit.cx(0, 1)
        self.state_vector = Statevector.from_dict({'00': 1, '01': 0, '10': 0, '11': 0})

    def test_visualize_circuit(self):
        visualize_circuit(self.circuit)  # This will display the circuit

    def test_plot_histogram_data(self):
        counts = {'00': 500, '01': 300, '10': 200}
        plot_histogram_data(counts)  # This will display the histogram

    def test_plot_state_vector(self):
        plot_state_vector(self.state_vector)  # This will display the Q-sphere

    def test_circuit_to_matrix(self):
        matrix = circuit_to_matrix(self.circuit)
        self.assertEqual(matrix.shape, (4, 4))

    def test_matrix_to_circuit(self):
        matrix = random_unitary(2)
        circuit = matrix_to_circuit(matrix)
        self.assertEqual(circuit.num_qubits, 2)

    def test_random_unitary(self):
        unitary = random_unitary(2)
        self.assertEqual(unitary.shape, (4, 4))

    def test_fidelity(self):
        fidelity_value = fidelity(self.state_vector, self.state_vector)
        self.assertAlmostEqual(fidelity_value, 1.0)

    def test_normalize_vector(self):
        vector = np.array([1, 2, 3])
        normalized = normalize_vector(vector)
        self.assertAlmostEqual(np.linalg.norm(normalized), 1.0)

if __name__ == '__main__':
    unittest.main()

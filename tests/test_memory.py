"""
Unit Tests for Quantum Cosmic Memory Fabric (QCMF).
"""
import unittest
import numpy as np
from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import Statevector

class QuantumCosmicMemoryFabric:
    def __init__(self, n_qubits: int):
        """
        Initialize the Quantum Cosmic Memory Fabric.

        Args:
            n_qubits (int): Number of qubits for the memory fabric.
        """
        self.n_qubits = n_qubits
        self.memory = {}
        self.backend = Aer.get_backend('statevector_simulator')

    def store_state(self, address: int, state: Statevector):
        """Store a quantum state at a specified address."""
        self.memory[address] = state

    def retrieve_state(self, address: int) -> Statevector:
        """Retrieve a quantum state from a specified address."""
        if address not in self.memory:
            raise ValueError("Address not found in memory.")
        return self.memory[address]

    def create_random_state(self) -> Statevector:
        """Create a random quantum state."""
        circuit = QuantumCircuit(self.n_qubits)
        for qubit in range(self.n_qubits):
            circuit.h(qubit)  # Apply Hadamard gate to create superposition
        return self.simulate_circuit(circuit)

    def simulate_circuit(self, circuit: QuantumCircuit) -> Statevector:
        """Simulate the quantum circuit and return the resulting state."""
        result = execute(circuit, self.backend).result()
        return result.get_statevector()

    def clear_memory(self):
        """Clear the memory fabric."""
        self.memory.clear()

class TestQuantumCosmicMemoryFabric(unittest.TestCase):
    def setUp(self):
        """Set up the Quantum Cosmic Memory Fabric for testing."""
        self.qcmf = QuantumCosmicMemoryFabric(n_qubits=3)

    def test_store_and_retrieve_state(self):
        """Test storing and retrieving a quantum state."""
        state = self.qcmf.create_random_state()
        address = 0
        self.qcmf.store_state(address, state)
        retrieved_state = self.qcmf.retrieve_state(address)
        np.testing.assert_array_almost_equal(retrieved_state, state)

    def test_retrieve_nonexistent_state(self):
        """Test retrieving a state from a nonexistent address."""
        with self.assertRaises(ValueError):
            self.qcmf.retrieve_state(999)  # Address not found

    def test_clear_memory(self):
        """Test clearing the memory fabric."""
        state1 = self.qcmf.create_random_state()
        state2 = self.qcmf.create_random_state()
        self.qcmf.store_state(0, state1)
        self.qcmf.store_state(1, state2)
        self.qcmf.clear_memory()
        self.assertEqual(len(self.qcmf.memory), 0)  # Memory should be empty

    def test_create_random_state(self):
        """Test creating a random quantum state."""
        state = self.qcmf.create_random_state()
        self.assertEqual(state.shape[0], 8)  # 3 qubits -> 8 basis states

# Run the tests
if __name__ == "__main__":
    unittest.main()

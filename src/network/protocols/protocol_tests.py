import unittest
import numpy as np
from .qkd_bb84 import BB84Protocol
from .teleportation import QuantumTeleportation
from .entanglement_routing import EntanglementRouting
from .protocol_utils import random_bit_string, measure_qubit
from .p2p_protocol import P2PProtocol

class TestQuantumProtocols(unittest.TestCase):

    def setUp(self):
        """Set up test variables."""
        self.bb84 = BB84Protocol(num_bits=10)
        self.teleportation = QuantumTeleportation()
        self.routing = EntanglementRouting()
        self.p2p = P2PProtocol()

    def test_bb84_key_generation(self):
        """Test the key generation in BB84 protocol."""
        key = self.bb84.generate_key()
        self.assertEqual(len(key), 10)  # Ensure the key length is correct
        self.assertTrue(all(bit in [0, 1] for bit in key))  # Ensure all bits are valid

    def test_teleportation(self):
        """Test the teleportation of a quantum state."""
        state = np.array([1, 0])  # Example state |0>
        teleported_state = self.teleportation.teleport(state, bell_state='Φ+')
        np.testing.assert_array_almost_equal(teleported_state, state)  # Check if the state is preserved

        # Test teleportation with a different state
        state = np.array([0, 1])  # Example state |1>
        teleported_state = self.teleportation.teleport(state, bell_state='Φ+')
        np.testing.assert_array_almost_equal(teleported_state, state)  # Check if the state is preserved

    def test_entanglement_routing(self):
        """Test the establishment of entanglement routes."""
        self.routing.add_node('NodeA')
        self.routing.add_node('NodeB')
        self.routing.establish_route('NodeA', 'NodeB')
        self.assertTrue(self.routing.is_route_established('NodeA', 'NodeB'))  # Check if route is established

        # Test removing a route
        self.routing.remove_route('NodeA', 'NodeB')
        self.assertFalse(self.routing.is_route_established('NodeA', 'NodeB'))  # Check if route is removed

    def test_random_bit_string(self):
        """Test the generation of a random bit string."""
        bit_string = random_bit_string(8)
        self.assertEqual(len(bit_string), 8)  # Ensure the bit string length is correct
        self.assertTrue(all(bit in [0, 1] for bit in bit_string))  # Check if all bits are 0 or 1

    def test_measure_qubit(self):
        """Test the measurement of a qubit."""
        state = np.array([1, 0])  # Example state |0>
        measured = measure_qubit(state, 'Z')
        self.assertEqual(measured, 0)  # Measurement in Z basis should return 0

        state = np.array([0, 1])  # Example state |1>
        measured = measure_qubit(state, 'Z')
        self.assertEqual(measured, 1)  # Measurement in Z basis should return 1

        # Test measurement in X basis
        state = np.array([1/np.sqrt(2), 1/np.sqrt(2)])  # Example state |+>
        measured = measure_qubit(state, 'X')
        self.assertIn(measured, [0, 1])  # Measurement in X basis should return either 0 or 1

    def test_p2p_protocol(self):
        """Test the P2P protocol for node connections."""
        self.p2p.connect('NodeA', 'NodeB')
        self.assertTrue(self.p2p.is_connected('NodeA', 'NodeB'))  # Check if nodes are connected

        self.p2p.disconnect('NodeA', 'NodeB')
        self.assertFalse(self.p2p.is_connected('NodeA', 'NodeB'))  # Check if nodes are disconnected

        # Test connecting non-existent nodes
        with self.assertRaises(KeyError):
            self.p2p.disconnect('NodeA', 'NodeC')  # Should raise an error since NodeC is not connected

if __name__ == "__main__":
    unittest.main()

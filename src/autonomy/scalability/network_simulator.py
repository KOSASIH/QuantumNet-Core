"""
Network Simulator for Advanced Network Topology and Performance Analysis.
This module simulates network behavior, allowing for dynamic node interactions,
topology management, and performance evaluation.
"""

import numpy as np
import random

class NetworkNode:
    def __init__(self, node_id: int, capacity: float):
        """
        Initialize a network node.

        Args:
            node_id (int): Unique identifier for the node.
            capacity (float): Maximum capacity of the node.
        """
        self.node_id = node_id
        self.capacity = capacity
        self.current_load = 0.0

    def add_load(self, load: float):
        """Add load to the node, ensuring it does not exceed capacity."""
        if self.current_load + load <= self.capacity:
            self.current_load += load
        else:
            raise ValueError("Load exceeds node capacity.")

    def reset_load(self):
        """Reset the current load of the node."""
        self.current_load = 0.0

class Network:
    def __init__(self):
        """Initialize the network with an empty list of nodes and connections."""
        self.nodes = {}
        self.connections = {}

    def add_node(self, node: NetworkNode):
        """Add a node to the network."""
        self.nodes[node.node_id] = node

    def connect_nodes(self, node_id1: int, node_id2: int):
        """Create a connection between two nodes."""
        if node_id1 in self.nodes and node_id2 in self.nodes:
            if node_id1 not in self.connections:
                self.connections[node_id1] = []
            self.connections[node_id1].append(node_id2)

    def simulate_traffic(self, traffic_pattern: dict):
        """Simulate network traffic based on a given traffic pattern.

        Args:
            traffic_pattern (dict): A dictionary where keys are node IDs and values are loads to be added.
        """
        for node_id, load in traffic_pattern.items():
            if node_id in self.nodes:
                self.nodes[node_id].add_load(load)

    def evaluate_performance(self) -> float:
        """Evaluate the overall performance of the network based on node loads.

        Returns:
            float: The average load across all nodes.
        """
        total_load = sum(node.current_load for node in self.nodes.values())
        return total_load / len(self.nodes) if self.nodes else 0.0

    def reset_network(self):
        """Reset all nodes in the network."""
        for node in self.nodes.values():
            node.reset_load()

# Example usage
if __name__ == "__main__":
    network = Network()

    # Create and add nodes to the network
    for i in range(5):
        node = NetworkNode(node_id=i, capacity=random.uniform(50, 100))
        network.add_node(node)

    # Connect nodes randomly
    for i in range(5):
        for j in range(i + 1, 5):
            if random.choice([True, False]):
                network.connect_nodes(i, j)

    # Simulate traffic
    traffic_pattern = {i: random.uniform(10, 30) for i in range(5)}
    network.simulate_traffic(traffic_pattern)

    # Evaluate performance
    avg_load = network.evaluate_performance()
    print("Average Load in Network:", avg_load)

    # Reset network for next simulation
    network.reset_network()

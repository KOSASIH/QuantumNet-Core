"""
Utilities for the Quantum Infinite Scalability Framework (QISF).
This module provides functions for generating network topologies,
calculating performance metrics, and visualizing network structures.
"""

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def generate_random_topology(num_nodes: int, density: float) -> np.ndarray:
    """
    Generate a random network topology as an adjacency matrix.

    Args:
        num_nodes (int): The number of nodes in the network.
        density (float): The probability of edge creation between nodes.

    Returns:
        np.ndarray: The generated network topology as an adjacency matrix.
    """
    topology = np.random.rand(num_nodes, num_nodes) < density
    np.fill_diagonal(topology, 0)  # No self-loops
    return topology.astype(float)

def calculate_network_efficiency(topology: np.ndarray) -> float:
    """
    Calculate the efficiency of the network based on the topology.

    Args:
        topology (np.ndarray): The network topology as an adjacency matrix.

    Returns:
        float: The efficiency score of the network.
    """
    G = nx.from_numpy_array(topology)
    efficiency = nx.global_efficiency(G)
    return efficiency

def visualize_topology(topology: np.ndarray, title: str = "Network Topology"):
    """
    Visualize the network topology using Matplotlib and NetworkX.

    Args:
        topology (np.ndarray): The network topology as an adjacency matrix.
        title (str): The title of the visualization.
    """
    G = nx.from_numpy_array(topology)
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G)  # positions for all nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)
    nx.draw_networkx_edges(G, pos, width=2)
    nx.draw_networkx_labels(G, pos, font_size=12)
    plt.title(title)
    plt.axis('off')  # Turn off the axis
    plt.show()

def save_topology_to_file(topology: np.ndarray, filename: str):
    """
    Save the network topology to a file in a human-readable format.

    Args:
        topology (np.ndarray): The network topology as an adjacency matrix.
        filename (str): The name of the file to save the topology.
    """
    np.savetxt(filename, topology, fmt='%.2f')
    print(f"Topology saved to {filename}")

def load_topology_from_file(filename: str) -> np.ndarray:
    """
    Load a network topology from a file.

    Args:
        filename (str): The name of the file to load the topology from.

    Returns:
        np.ndarray: The loaded network topology as an adjacency matrix.
    """
    topology = np.loadtxt(filename)
    return topology

# Example usage
if __name__ == "__main__":
    num_nodes = 10
    density = 0.3

    # Generate a random topology
    topology = generate_random_topology(num_nodes, density)
    print("Generated Topology:\n", topology)

    # Calculate network efficiency
    efficiency = calculate_network_efficiency(topology)
    print("Network Efficiency:", efficiency)

    # Visualize the topology
    visualize_topology(topology)

    # Save the topology to a file
    save_topology_to_file(topology, "network_topology.txt")

    # Load the topology from a file
    loaded_topology = load_topology_from_file("network_topology.txt")
    print("Loaded Topology:\n", loaded_topology)

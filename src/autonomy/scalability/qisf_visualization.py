"""
Visualization utilities for the Quantum Infinite Scalability Framework (QISF).
This module provides functions for visualizing network topologies and performance metrics.
"""

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def visualize_topology(topology: np.ndarray, title: str = "Network Topology", node_sizes: np.ndarray = None):
    """
    Visualize the network topology using Matplotlib and NetworkX.

    Args:
        topology (np.ndarray): The network topology as an adjacency matrix.
        title (str): The title of the visualization.
        node_sizes (np.ndarray): Optional sizes for the nodes based on their load or capacity.
    """
    G = nx.from_numpy_array(topology)
    
    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(G, seed=42)  # positions for all nodes
    if node_sizes is None:
        node_sizes = np.ones(G.number_of_nodes()) * 300  # Default node size

    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='skyblue', alpha=0.7)
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=12, font_color='black')
    
    plt.title(title, fontsize=16)
    plt.axis('off')  # Turn off the axis
    plt.show()

def visualize_performance(topology: np.ndarray, performance_metrics: np.ndarray, title: str = "Network Performance"):
    """
    Visualize the performance metrics of the network.

    Args:
        topology (np.ndarray): The network topology as an adjacency matrix.
        performance_metrics (np.ndarray): The performance metrics for each node.
        title (str): The title of the visualization.
    """
    G = nx.from_numpy_array(topology)
    
    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(G, seed=42)  # positions for all nodes
    node_sizes = performance_metrics * 1000  # Scale performance metrics for visualization

    nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color='lightgreen', alpha=0.7)
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=12, font_color='black')
    
    plt.title(title, fontsize=16)
    plt.axis('off')  # Turn off the axis
    plt.show()

def save_visualization(topology: np.ndarray, filename: str):
    """
    Save the network topology visualization to a file.

    Args:
        topology (np.ndarray): The network topology as an adjacency matrix.
        filename (str): The name of the file to save the visualization.
    """
    G = nx.from_numpy_array(topology)
    plt.figure(figsize=(12, 10))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=300, font_size=12)
    
    plt.title("Network Topology", fontsize=16)
    plt.axis('off')
    plt.savefig(filename, format='PNG')
    plt.close()
    print(f"Visualization saved to {filename}")

# Example usage
if __name__ == "__main__":
    # Generate a random topology for demonstration
    num_nodes = 10
    density = 0.3
    topology = np.random.rand(num_nodes, num_nodes) < density
    np.fill_diagonal(topology, 0)  # No self-loops
    topology = topology.astype(float)

    # Visualize the topology
    visualize_topology(topology)

    # Simulate performance metrics for demonstration
    performance_metrics = np.random.rand(num_nodes)  # Random performance metrics
    visualize_performance(topology, performance_metrics)

    # Save the visualization to a file
    save_visualization(topology, "network_topology_visualization.png")

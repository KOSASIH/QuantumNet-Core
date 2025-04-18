import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QuantumRepeater:
    def __init__(self):
        self.entangled_pairs = {}  # Store entangled pairs as {(node_a, node_b): True}
        self.nodes = set()  # Keep track of all nodes

    def add_node(self, node):
        """Add a node to the repeater network."""
        self.nodes.add(node)
        logging.info(f"Node {node} added to the repeater network.")

    def remove_node(self, node):
        """Remove a node from the network and its associated entangled pairs."""
        if node in self.nodes:
            self.nodes.remove(node)
            # Remove all entangled pairs associated with this node
            self.entangled_pairs = {k: v for k, v in self.entangled_pairs.items() if node not in k}
            logging.info(f"Node {node} removed from the repeater network.")
        else:
            logging.warning(f"Node {node} does not exist in the network.")

    def create_entangled_pair(self, node_a, node_b):
        """Create an entangled pair between two nodes."""
        if node_a not in self.nodes or node_b not in self.nodes:
            raise ValueError("Both nodes must be part of the network.")
        self.entangled_pairs[(node_a, node_b)] = True
        self.entangled_pairs[(node_b, node_a)] = True  # Ensure bidirectional entanglement
        logging.info(f"Entangled pair created between {node_a} and {node_b}.")

    def remove_entangled_pair(self, node_a, node_b):
        """Remove an entangled pair between two nodes."""
        if (node_a, node_b) in self.entangled_pairs:
            del self.entangled_pairs[(node_a, node_b)]
            del self.entangled_pairs[(node_b, node_a)]  # Ensure bidirectional removal
            logging.info(f"Entangled pair removed between {node_a} and {node_b}.")
        else:
            logging.warning(f"No entangled pair exists between {node_a} and {node_b}.")

    def relay(self, node_a, node_b):
        """Relay quantum information between two nodes using entanglement."""
        if (node_a, node_b) in self.entangled_pairs:
            logging.info(f"Relaying information from {node_a} to {node_b}.")
            return True  # Indicate successful relay
        else:
            logging.warning(f"Failed to relay information from {node_a} to {node_b}. No entangled pair exists.")
            return False  # Indicate failure to relay

    def find_path(self, start_node, end_node, path=[]):
        """Find a path between two nodes using Depth-First Search (DFS)."""
        path = path + [start_node]
        if start_node == end_node:
            return path
        if start_node not in self.nodes:
            return None
        for (node_a, node_b) in self.entangled_pairs.keys():
            if start_node in (node_a, node_b):
                next_node = node_b if node_a == start_node else node_a
                if next_node not in path:
                    new_path = self.find_path(next_node, end_node, path)
                    if new_path:
                        return new_path
        return None

# Example usage
if __name__ == "__main__":
    repeater = QuantumRepeater()
    repeater.add_node('NodeA')
    repeater.add_node('NodeB')
    repeater.add_node('NodeC')

    repeater.create_entangled_pair('NodeA', 'NodeB')
    repeater.create_entangled_pair('NodeB', 'NodeC')

    print("Relay from NodeA to NodeB:", repeater.relay('NodeA', 'NodeB'))  # Should succeed
    print("Relay from NodeA to NodeC:", repeater.relay('NodeA', 'NodeC'))  # Should fail

    path = repeater.find_path('NodeA', 'NodeC')
    print("Path from NodeA to NodeC:", path)  # Should show a path if it exists

    repeater.remove_entangled_pair('NodeA', 'NodeB')
    print("Relay from NodeA to NodeB after removal:", repeater.relay('NodeA', 'NodeB'))  # Should fail

    repeater.remove_node('NodeB')
    print("Relay from NodeA to NodeC after removing NodeB:", repeater.relay('NodeA', 'NodeC'))  # Should still fail
    print("Current entangled pairs:", repeater.entangled_pairs)  # Should show remaining pairs

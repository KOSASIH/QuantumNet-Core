import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EntanglementRouting:
    def __init__(self):
        self.routes = {}
        self.nodes = set()  # Keep track of all nodes

    def add_node(self, node):
        """Add a node to the network."""
        self.nodes.add(node)
        logging.info(f"Node {node} added to the network.")

    def remove_node(self, node):
        """Remove a node from the network and its associated routes."""
        if node in self.nodes:
            self.nodes.remove(node)
            # Remove all routes associated with this node
            self.routes = {k: v for k, v in self.routes.items() if node not in k}
            logging.info(f"Node {node} removed from the network.")
        else:
            logging.warning(f"Node {node} does not exist in the network.")

    def establish_route(self, node_a, node_b):
        """Establish an entanglement route between two nodes."""
        if node_a not in self.nodes or node_b not in self.nodes:
            raise ValueError("Both nodes must be part of the network.")
        self.routes[(node_a, node_b)] = True
        self.routes[(node_b, node_a)] = True  # Ensure bidirectional route
        logging.info(f"Entanglement route established between {node_a} and {node_b}.")

    def remove_route(self, node_a, node_b):
        """Remove an entanglement route between two nodes."""
        if (node_a, node_b) in self.routes:
            del self.routes[(node_a, node_b)]
            del self.routes[(node_b, node_a)]  # Ensure bidirectional removal
            logging.info(f"Entanglement route removed between {node_a} and {node_b}.")
        else:
            logging.warning(f"No route exists between {node_a} and {node_b}.")

    def is_route_established(self, node_a, node_b):
        """Check if an entanglement route is established."""
        return self.routes.get((node_a, node_b), False)

    def find_path(self, start_node, end_node, path=[]):
        """Find a path between two nodes using Depth-First Search (DFS)."""
        path = path + [start_node]
        if start_node == end_node:
            return path
        if start_node not in self.nodes:
            return None
        for node in self.routes:
            if start_node in node:
                next_node = node[1] if node[0] == start_node else node[0]
                if next_node not in path:
                    new_path = self.find_path(next_node, end_node, path)
                    if new_path:
                        return new_path
        return None

# Example usage
if __name__ == "__main__":
    routing = EntanglementRouting()
    routing.add_node('NodeA')
    routing.add_node('NodeB')
    routing.add_node('NodeC')

    routing.establish_route('NodeA', 'NodeB')
    routing.establish_route('NodeB', 'NodeC')

    print("Is route established between NodeA and NodeB?", routing.is_route_established('NodeA', 'NodeB'))
    print("Path from NodeA to NodeC:", routing.find_path('NodeA', 'NodeC'))

    routing.remove_route('NodeA', 'NodeB')
    print("Is route established between NodeA and NodeB after removal?", routing.is_route_established('NodeA', 'NodeB'))

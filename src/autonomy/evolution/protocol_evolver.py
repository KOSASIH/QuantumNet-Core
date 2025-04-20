import numpy as np
import logging
import matplotlib.pyplot as plt

# Set up logging
logging.basicConfig(level=logging.INFO)

class ProtocolEvolver:
    def __init__(self, initial_protocol):
        self.current_protocol = initial_protocol
        self.evolution_history = []

    def evolve(self, generations=10):
        """Evolve the current network protocol over a number of generations."""
        for generation in range(generations):
            logging.info(f"Evolution Generation {generation + 1}")
            new_protocol = self.mutate(self.current_protocol)
            if self.evaluate_protocol(new_protocol) > self.evaluate_protocol(self.current_protocol):
                self.current_protocol = new_protocol
                logging.info("Protocol improved.")
            else:
                logging.info("No improvement in protocol.")
            self.evolution_history.append(self.evaluate_protocol(self.current_protocol))

    def mutate(self, protocol):
        """Mutate the current protocol by randomly changing states or transitions."""
        mutated_protocol = protocol.copy()
        mutation_type = np.random.choice(['add_state', 'remove_state', 'change_transition'])

        if mutation_type == 'add_state':
            new_state = self.random_state()
            mutated_protocol['states'].append(new_state)
            logging.info(f"Added state: {new_state}")
        elif mutation_type == 'remove_state' and len(mutated_protocol['states']) > 0:
            removed_state = mutated_protocol['states'].pop(np.random.randint(len(mutated_protocol['states'])))
            logging.info(f"Removed state: {removed_state}")
        elif mutation_type == 'change_transition' and len(mutated_protocol['transitions']) > 0:
            index = np.random.randint(len(mutated_protocol['transitions']))
            old_transition = mutated_protocol['transitions'][index]
            mutated_protocol['transitions'][index] = self.random_transition()
            logging.info(f"Changed transition: {old_transition} to {mutated_protocol['transitions'][index]}")

        return mutated_protocol

    def random_state(self):
        """Generate a random state for the protocol."""
        return f"State_{np.random.randint(100)}"  # Example state representation

    def random_transition(self):
        """Generate a random transition for the protocol."""
        return f"Transition_{np.random.randint(100)}"  # Example transition representation

    def evaluate_protocol(self, protocol=None):
        """Evaluate the performance of the current protocol."""
        if protocol is None:
            protocol = self.current_protocol
        # Placeholder for actual evaluation logic
        # For demonstration, we will return a score based on the number of states and transitions
        return len(protocol['states']) + len(protocol['transitions'])  # Example performance score

    def plot_evolution(self):
        """Plot the evolution of protocol performance over generations."""
        plt.plot(self.evolution_history)
        plt.title('Protocol Performance Over Generations')
        plt.xlabel('Generation')
        plt.ylabel('Performance Score')
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    initial_protocol = {
        'states': ['State_0', 'State_1'],
        'transitions': ['Transition_0', 'Transition_1']
    }
    protocol_evolver = ProtocolEvolver(initial_protocol)
    protocol_evolver.evolve(generations=20)
    print("Final Protocol:", protocol_evolver.current_protocol)
    protocol_evolver.plot_evolution()

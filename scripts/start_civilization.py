"""
Script for Launching Autonomous Quantum Civilization Synthesizer (AQCS).
"""
import numpy as np
import matplotlib.pyplot as plt

class AutonomousQuantumCivilizationSynthesizer:
    def __init__(self, civilization_size: int):
        """
        Initialize the Autonomous Quantum Civilization Synthesizer.

        Args:
            civilization_size (int): Number of entities in the civilization.
        """
        self.civilization_size = civilization_size
        self.civilization_data = []

    def synthesize_civilization(self):
        """Synthesize a new civilization with random attributes."""
        self.civilization_data = [
            {
                'entity_id': i,
                'resources': np.random.randint(1, 100),
                'technology_level': np.random.uniform(0, 1),
                'happiness': np.random.uniform(0, 1)
            }
            for i in range(self.civilization_size)
        ]
        return self.civilization_data

    def manage_resources(self):
        """Manage resources among the civilization entities."""
        for entity in self.civilization_data:
            # Simple resource management logic: redistribute resources
            entity['resources'] += np.random.randint(-10, 10)
            entity['resources'] = max(entity['resources'], 0)  # Ensure resources are non-negative

    def evaluate_civilization(self):
        """Evaluate the overall status of the civilization."""
        total_resources = sum(entity['resources'] for entity in self.civilization_data)
        average_technology = np.mean([entity['technology_level'] for entity in self.civilization_data])
        average_happiness = np.mean([entity['happiness'] for entity in self.civilization_data])
        return {
            'total_resources': total_resources,
            'average_technology': average_technology,
            'average_happiness': average_happiness
        }

    def visualize_civilization(self):
        """Visualize the civilization data."""
        ids = [entity['entity_id'] for entity in self.civilization_data]
        resources = [entity['resources'] for entity in self.civilization_data]
        technology_levels = [entity['technology_level'] for entity in self.civilization_data]
        happiness_levels = [entity['happiness'] for entity in self.civilization_data]

        x = np.arange(len(ids))  # the label locations
        width = 0.2  # the width of the bars

        fig, ax = plt.subplots()
        bars1 = ax.bar(x - width, resources, width, label='Resources')
        bars2 = ax.bar(x, technology_levels, width, label='Technology Level')
        bars3 = ax.bar(x + width, happiness_levels, width, label='Happiness Level')

        ax.set_xlabel('Entity ID')
        ax.set_ylabel('Values')
        ax.set_title('Civilization Data Overview')
        ax.set_xticks(x)
        ax.set_xticklabels(ids)
        ax.legend()

        plt.show()

def main():
    # Initialize the Autonomous Quantum Civilization Synthesizer
    civilization_size = 10  # Example: 10 entities
    aqcs = AutonomousQuantumCivilizationSynthesizer(civilization_size)

    # Synthesize a new civilization
    civilization = aqcs.synthesize_civilization()
    print("Synthesized Civilization Data:")
    for entity in civilization:
        print(entity)

    # Manage resources among the civilization entities
    aqcs.manage_resources()
    print("\nAfter Resource Management:")
    for entity in aqcs.civilization_data:
        print(entity)

    # Evaluate the overall status of the civilization
    evaluation = aqcs.evaluate_civilization()
    print("\nCivilization Evaluation:")
    print(evaluation)

    # Visualize the civilization data
    aqcs.visualize_civilization()

if __name__ == "__main__":
    main()

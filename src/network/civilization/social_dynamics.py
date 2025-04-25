"""
Agent-Based Model for Social Dynamics Simulation.
"""
import numpy as np
import random

class Agent:
    def __init__(self, id: int, position: np.ndarray, social_tendency: float):
        """
        Initialize an agent with an ID, position, and social tendency.

        Args:
            id (int): Unique identifier for the agent.
            position (np.ndarray): Initial position of the agent in the environment.
            social_tendency (float): Tendency of the agent to interact socially.
        """
        self.id = id
        self.position = position
        self.social_tendency = social_tendency
        self.state = 'neutral'  # Possible states: 'neutral', 'happy', 'sad'

    def move(self, bounds: np.ndarray):
        """Move the agent randomly within the defined bounds."""
        self.position += np.random.uniform(-1, 1, size=self.position.shape)
        self.position = np.clip(self.position, 0, bounds)

    def interact(self, other_agent):
        """Interact with another agent based on social tendency."""
        if random.random() < self.social_tendency:
            # Simple interaction logic: change state based on the other agent's state
            if other_agent.state == 'happy':
                self.state = 'happy'
            elif other_agent.state == 'sad':
                self.state = 'sad'

class SocialDynamics:
    def __init__(self, num_agents: int, bounds: np.ndarray):
        """
        Initialize the social dynamics simulation.

        Args:
            num_agents (int): Number of agents in the simulation.
            bounds (np.ndarray): The bounds of the simulation environment.
        """
        self.agents = [Agent(i, np.random.rand(2) * bounds, random.uniform(0.1, 1.0)) for i in range(num_agents)]
        self.bounds = bounds

    def step(self):
        """Perform a single step in the simulation."""
        for agent in self.agents:
            agent.move(self.bounds)
            for other_agent in self.agents:
                if agent.id != other_agent.id:
                    agent.interact(other_agent)

    def run(self, steps: int):
        """Run the simulation for a specified number of steps."""
        for step in range(steps):
            self.step()
            if step % 10 == 0:
                self.report_status(step)

    def report_status(self, step: int):
        """Report the status of the agents at a given step."""
        states = [agent.state for agent in self.agents]
        print(f"Step {step}: Agent States: {states}")

# Example usage
if __name__ == "__main__":
    num_agents = 100
    bounds = np.array([10, 10])
    simulation = SocialDynamics(num_agents, bounds)

    # Run the simulation for 100 steps
    simulation.run(100)

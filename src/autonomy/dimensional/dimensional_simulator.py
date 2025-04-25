"""
Dimensional Simulator for High-Dimensional Spacetime.
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class DimensionalSimulator:
    def __init__(self, dimensions: int):
        """
        Initialize the Dimensional Simulator.

        Args:
            dimensions (int): The number of dimensions for the simulation.
        """
        self.dimensions = dimensions

    def simulate_random_walk(self, steps: int) -> np.ndarray:
        """
        Simulate a random walk in high-dimensional space.

        Args:
            steps (int): The number of steps in the random walk.

        Returns:
            np.ndarray: The trajectory of the random walk.
        """
        # Initialize the starting point at the origin
        trajectory = np.zeros((steps, self.dimensions))
        
        for i in range(1, steps):
            # Generate a random step in each dimension
            step = np.random.normal(0, 1, self.dimensions)
            trajectory[i] = trajectory[i - 1] + step  # Update position

        return trajectory

    def visualize_trajectory(self, trajectory: np.ndarray):
        """
        Visualize the trajectory of the random walk.

        Args:
            trajectory (np.ndarray): The trajectory to visualize.
        """
        if self.dimensions == 2:
            plt.figure(figsize=(8, 6))
            plt.plot(trajectory[:, 0], trajectory[:, 1], marker='o', markersize=2)
            plt.title("2D Random Walk Trajectory")
            plt.xlabel("X-axis")
            plt.ylabel("Y-axis")
            plt.grid()
            plt.axis('equal')
            plt.show()
        elif self.dimensions == 3:
            fig = plt.figure(figsize=(8, 6))
            ax = fig.add_subplot(111, projection='3d')
            ax.plot(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2], marker='o', markersize=2)
            ax.set_title("3D Random Walk Trajectory")
            ax.set_xlabel("X-axis")
            ax.set_ylabel("Y-axis")
            ax.set_zlabel("Z-axis")
            plt.show()
        else:
            print("Visualization is only supported for 2D and 3D trajectories.")

# Example usage
if __name__ == "__main__":
    dimensions = 3  # Change to 2 for 2D simulation
    steps = 1000
    simulator = DimensionalSimulator(dimensions)

    # Simulate a random walk
    trajectory = simulator.simulate_random_walk(steps)

    # Visualize the trajectory
    simulator.visualize_trajectory(trajectory)

"""
Visualization Utilities for Autonomous Quantum Dimensional Navigator (AQDN).
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D

class AQDNVisualization:
    @staticmethod
    def plot_high_dimensional_data(data: np.ndarray, title: str = "High-Dimensional Data"):
        """
        Visualize high-dimensional data in 2D or 3D.

        Args:
            data (np.ndarray): The data to visualize.
            title (str): The title of the plot.
        """
        if data.shape[1] == 2:
            plt.figure(figsize=(8, 6))
            plt.scatter(data[:, 0], data[:, 1], alpha=0.7)
            plt.title(title)
            plt.xlabel("Dimension 1")
            plt.ylabel("Dimension 2")
            plt.grid()
            plt.axis('equal')
            plt.show()
        elif data.shape[1] == 3:
            fig = plt.figure(figsize=(8, 6))
            ax = fig.add_subplot(111, projection='3d')
            ax.scatter(data[:, 0], data[:, 1], data[:, 2], alpha=0.7)
            ax.set_title(title)
            ax.set_xlabel("Dimension 1")
            ax.set_ylabel("Dimension 2")
            ax.set_zlabel("Dimension 3")
            plt.show()
        else:
            print("Visualization is only supported for 2D and 3D data.")

    @staticmethod
    def plot_projection(data: np.ndarray, basis: np.ndarray, title: str = "Projection onto Subspace"):
        """
        Visualize the projection of data onto a subspace defined by the basis.

        Args:
            data (np.ndarray): The original data.
            basis (np.ndarray): The basis vectors defining the subspace.
            title (str): The title of the plot.
        """
        projected_data = data @ basis @ np.linalg.pinv(basis)
        AQDNVisualization.plot_high_dimensional_data(projected_data, title)

    @staticmethod
    def plot_covariance_matrix(cov_matrix: np.ndarray, title: str = "Covariance Matrix"):
        """
        Visualize the covariance matrix as a heatmap.

        Args:
            cov_matrix (np.ndarray): The covariance matrix to visualize.
            title (str): The title of the plot.
        """
        plt.figure(figsize=(8, 6))
        sns.heatmap(cov_matrix, annot=True, fmt=".2f", cmap='viridis', square=True)
        plt.title(title)
        plt.xlabel("Features")
        plt.ylabel("Features")
        plt.colorbar(label='Covariance')
        plt.show()

    @staticmethod
    def plot_distance_matrix(distance_matrix: np.ndarray, title: str = "Distance Matrix"):
        """
        Visualize the distance matrix as a heatmap.

        Args:
            distance_matrix (np.ndarray): The distance matrix to visualize.
            title (str): The title of the plot.
        """
        plt.figure(figsize=(8, 6))
        sns.heatmap(distance_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True)
        plt.title(title)
        plt.xlabel("Points")
        plt.ylabel("Points")
        plt.colorbar(label='Distance')
        plt.show()

# Example usage
if __name__ == "__main__":
    from aqdn_utils import AQDNUtils

    # Generate random high-dimensional data
    num_points = 100
    dimensions = 3
    random_data = AQDNUtils.generate_random_points(num_points, dimensions)

    # Visualize high-dimensional data
    AQDNVisualization.plot_high_dimensional_data(random_data)

    # Calculate and visualize covariance matrix
    covariance_matrix = AQDNUtils.calculate_covariance_matrix(random_data)
    AQDNVisualization.plot_covariance_matrix(covariance_matrix)

    # Calculate and visualize distance matrix
    distance_matrix = np.linalg.norm(random_data[:, np.newaxis] - random_data, axis=2)
    AQDNVisualization.plot_distance_matrix(distance_matrix)

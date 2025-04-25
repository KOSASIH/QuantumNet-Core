"""
Utilities for Autonomous Quantum Dimensional Navigator (AQDN).
"""
import numpy as np

class AQDNUtils:
    @staticmethod
    def normalize(data: np.ndarray) -> np.ndarray:
        """
        Normalize the input data.

        Args:
            data (np.ndarray): Input data to normalize.

        Returns:
            np.ndarray: Normalized data.
        """
        norm = np.linalg.norm(data)
        if norm == 0:
            return data  # Avoid division by zero
        return data / norm

    @staticmethod
    def calculate_distance(point1: np.ndarray, point2: np.ndarray) -> float:
        """
        Calculate the Euclidean distance between two points.

        Args:
            point1 (np.ndarray): First point in space.
            point2 (np.ndarray): Second point in space.

        Returns:
            float: Euclidean distance between the two points.
        """
        return np.linalg.norm(point1 - point2)

    @staticmethod
    def generate_random_points(num_points: int, dimensions: int) -> np.ndarray:
        """
        Generate random points in a high-dimensional space.

        Args:
            num_points (int): Number of random points to generate.
            dimensions (int): Number of dimensions for each point.

        Returns:
            np.ndarray: Array of random points of shape (num_points, dimensions).
        """
        return np.random.rand(num_points, dimensions)

    @staticmethod
    def project_onto_subspace(data: np.ndarray, basis: np.ndarray) -> np.ndarray:
        """
        Project data onto a given subspace defined by the basis.

        Args:
            data (np.ndarray): Data points to project.
            basis (np.ndarray): Basis vectors defining the subspace.

        Returns:
            np.ndarray: Projected data points.
        """
        return data @ basis @ np.linalg.pinv(basis)

    @staticmethod
    def calculate_covariance_matrix(data: np.ndarray) -> np.ndarray:
        """
        Calculate the covariance matrix of the data.

        Args:
            data (np.ndarray): Input data of shape (n_samples, n_features).

        Returns:
            np.ndarray: Covariance matrix of shape (n_features, n_features).
        """
        return np.cov(data, rowvar=False)

# Example usage
if __name__ == "__main__":
    num_points = 5
    dimensions = 3
    random_points = AQDNUtils.generate_random_points(num_points, dimensions)
    print("Random Points:\n", random_points)

    normalized_points = AQDNUtils.normalize(random_points)
    print("Normalized Points:\n", normalized_points)

    point1 = np.array([1, 2, 3])
    point2 = np.array([4, 5, 6])
    distance = AQDNUtils.calculate_distance(point1, point2)
    print("Distance between points:", distance)

    covariance_matrix = AQDNUtils.calculate_covariance_matrix(random_points)
    print("Covariance Matrix:\n", covariance_matrix)

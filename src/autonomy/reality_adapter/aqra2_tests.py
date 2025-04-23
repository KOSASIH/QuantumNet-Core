### Updated `aqra2_tests.py`

import unittest
import numpy as np
from aqra2_utils import (
    preprocess_data,
    postprocess_data,
    save_data_to_csv,
    load_data_from_csv,
    calculate_statistics,
)
from aqra2_visualization import (
    plot_quantum_state_distribution,
    plot_correlation_matrix,
    plot_statistics,
    plot_3d_scatter,
)

class TestAQRA2Utils(unittest.TestCase):

    def test_preprocess_data(self):
        """Test the preprocessing of data."""
        data = np.array([1, 2, 3, 4, 5])
        preprocessed = preprocess_data(data)
        expected = np.array([0, 0.25, 0.5, 0.75, 1])
        np.testing.assert_array_almost_equal(preprocessed, expected)

    def test_postprocess_data(self):
        """Test the postprocessing of data."""
        data = np.array([0, 0.25, 0.5, 0.75, 1])
        postprocessed = postprocess_data(data)
        expected = np.array([0, 25, 50, 75, 100])
        np.testing.assert_array_almost_equal(postprocessed, expected)

    def test_calculate_statistics(self):
        """Test the calculation of statistics."""
        data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        stats = calculate_statistics(data)
        expected_mean = np.array([4, 5, 6])
        expected_variance = np.array([6, 6, 6])
        expected_std_dev = np.array([2.44948974, 2.44948974, 2.44948974])
        
        np.testing.assert_array_almost_equal(stats['mean'], expected_mean)
        np.testing.assert_array_almost_equal(stats['variance'], expected_variance)
        np.testing.assert_array_almost_equal(stats['std_dev'], expected_std_dev)

    def test_save_load_data(self):
        """Test saving and loading data from CSV."""
        data = np.array([[1, 2, 3], [4, 5, 6]])
        filename = 'test_data.csv'
        
        # Save data
        save_data_to_csv(data, filename)
        
        # Load data
        loaded_data = load_data_from_csv(filename)
        np.testing.assert_array_equal(loaded_data, data)

class TestAQRA2Visualization(unittest.TestCase):

    def test_plot_quantum_state_distribution(self):
        """Test if the quantum state distribution plot runs without errors."""
        data = np.random.rand(100)
        try:
            plot_quantum_state_distribution(data)
        except Exception as e:
            self.fail(f"plot_quantum_state_distribution raised an exception: {e}")

    def test_plot_correlation_matrix(self):
        """Test if the correlation matrix plot runs without errors."""
        data = np.random.rand(100, 3)
        try:
            plot_correlation_matrix(data)
        except Exception as e:
            self.fail(f"plot_correlation_matrix raised an exception: {e}")

    def test_plot_statistics(self):
        """Test if the statistics plot runs without errors."""
        statistics = {
            'mean': np.array([1, 2, 3]),
            'variance': np.array([0.5, 0.5, 0.5]),
            'std_dev': np.array([0.70710678, 0.70710678, 0.70710678]),
        }
        try:
            plot_statistics(statistics)
        except Exception as e:
            self.fail(f"plot_statistics raised an exception: {e}")

    def test_plot_3d_scatter(self):
        """Test if the 3D scatter plot runs without errors."""
        data = np.random.rand(100, 3)
        try:
            plot_3d_scatter(data)
        except Exception as e:
            self.fail(f"plot_3d_scatter raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()

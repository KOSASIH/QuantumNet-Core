# tests/test_utils.py

import unittest
from utils.math_utils import complex_to_polar, polar_to_complex

class TestMathUtils(unittest.TestCase):

    def test_complex_to_polar(self):
        """Test conversion from complex to polar coordinates."""
        complex_num = 1 + 1j
        magnitude, angle = complex_to_polar(complex_num)
        self.assertAlmostEqual(magnitude, 2**0.5)  # sqrt(2)
        self.assertAlmostEqual(angle, np.pi /  4)  # 45 degrees in radians

    def test_polar_to_complex(self):
        """Test conversion from polar to complex coordinates."""
        magnitude = 2
        angle = np.pi / 4  # 45 degrees in radians
        complex_num = polar_to_complex(magnitude, angle)
        self.assertAlmostEqual(complex_num.real, 1)
        self.assertAlmostEqual(complex_num.imag, 1)

if __name__ == "__main__":
    unittest.main()

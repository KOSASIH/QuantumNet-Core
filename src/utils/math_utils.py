# utils/math_utils.py

import numpy as np

def complex_to_polar(complex_num):
    """Converts a complex number to polar coordinates.
    
    Args:
        complex_num (complex): The complex number to convert.
    
    Returns:
        tuple: (magnitude, angle) in radians.
    """
    magnitude = np.abs(complex_num)
    angle = np.angle(complex_num)
    return magnitude, angle

def polar_to_complex(magnitude, angle):
    """Converts polar coordinates to a complex number.
    
    Args:
        magnitude (float): The magnitude of the complex number.
        angle (float): The angle in radians.
    
    Returns:
        complex: The corresponding complex number.
    """
    return magnitude * np.exp(1j * angle)

# Example usage
if __name__ == "__main__":
    polar = complex_to_polar(1 + 1j)
    print("Polar coordinates:", polar)
    complex_num = polar_to_complex(*polar)
    print("Complex number:", complex_num)

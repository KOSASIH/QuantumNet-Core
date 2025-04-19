import unittest
import numpy as np
from surface_code import SurfaceCode
from concatenated_code import ConcatenatedCode, SimpleInnerCode, SimpleOuterCode
from qec_utils import generate_random_errors, apply_errors, calculate_error_rate

class TestQuantumErrorCorrection(unittest.TestCase):
    
    def test_surface_code_initialization(self):
        sc = SurfaceCode(size=3)
        self.assertEqual(sc.size, 3)
        self.assertTrue((sc.qubits == 0).all())

    def test_apply_error(self):
        sc = SurfaceCode(size=3)
        sc.apply_error(1, 1)
        self.assertEqual(sc.qubits[1, 1], 1)

        # Test out of bounds error application
        with self.assertRaises(IndexError):
            sc.apply_error(3, 3)  # Out of bounds

    def test_measure_stabilizers(self):
        sc = SurfaceCode(size=3)
        sc.apply_error(1, 1)
        stabilizers = sc.measure_stabilizers()
        self.assertEqual(len(stabilizers), 9)  # 3x3 grid has 9 stabilizers

    def test_decode_errors(self):
        sc = SurfaceCode(size=3)
        sc.apply_error(1, 1)
        stabilizers = sc.measure_stabilizers()
        result = sc.decode_errors()
        self.assertIn("Errors detected", result)

    def test_concatenated_code(self):
        inner_code = SimpleInnerCode()
        outer_code = SimpleOuterCode()
        cc = ConcatenatedCode(outer_code=outer_code, inner_code=inner_code)
        
        encoded = cc.encode("Test")
        self.assertIn("Encoding", encoded)

        decoded = cc.decode(encoded)
        self.assertEqual(decoded, "Test")

    def test_error_rate_calculation(self):
        original = np.array([[0, 1], [1, 0]])
        errors = np.array([[0, 1], [0, 0]])
        corrupted = apply_errors(original, errors)
        error_rate = calculate_error_rate(original, corrupted)
        self.assertAlmostEqual(error_rate, 0.25)

    def test_random_error_generation(self):
        size = 5
        error_rate = 0.2
        errors = generate_random_errors(size, error_rate)
        self.assertEqual(errors.shape, (size, size))
        self.assertTrue(np.all((errors == 0) | (errors == 1)))

    def test_apply_random_errors(self):
        original_state = np.array([[0, 1], [1, 0]])
        error_rate = 0.5
        errors = generate_random_errors(2, error_rate)
        corrupted_state = apply_errors(original_state, errors)
        self.assertEqual(corrupted_state.shape, original_state.shape)

if __name__ == "__main__":
    unittest.main()

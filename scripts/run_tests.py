# scripts/run_tests.py

import unittest
import sys
import os

def discover_and_run_tests():
    """Discover and run all unit tests in the tests directory."""
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests')

    test_runner = unittest.TextTestRunner()
    result = test_runner.run(test_suite)

    if not result.wasSuccessful():
        print("Some tests failed.")
        sys.exit(1)
    else:
        print("All tests passed successfully.")

if __name__ == "__main__":
    discover_and_run_tests()

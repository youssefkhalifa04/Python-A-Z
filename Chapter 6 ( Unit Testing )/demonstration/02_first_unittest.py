"""Chapter 6 - First unittest example

This file shows how to write a test with the unittest module.
"""

import unittest


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(2 + 3, 5)

    def test_subtract(self):
        self.assertEqual(10 - 4, 6)


if __name__ == "__main__":
    unittest.main()

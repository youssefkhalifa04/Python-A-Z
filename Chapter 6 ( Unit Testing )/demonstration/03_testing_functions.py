"""Chapter 6 - Testing functions

This file shows how to test a small function with different inputs.
"""

import unittest


def is_even(number):
    return number % 2 == 0


class TestIsEven(unittest.TestCase):
    def test_even_number(self):
        self.assertTrue(is_even(8))

    def test_odd_number(self):
        self.assertFalse(is_even(7))


if __name__ == "__main__":
    unittest.main()

# Correction - Chapter 6 Exercises

## Exercise 1 - Testing a calculator
```python
import unittest


def multiply(a, b):
    return a * b


class TestMultiply(unittest.TestCase):
    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(0, 5), 0)


if __name__ == "__main__":
    unittest.main()
```

## Exercise 2 - Testing validation
```python
import unittest


def is_adult(age):
    return age >= 18


class TestIsAdult(unittest.TestCase):
    def test_is_adult_true(self):
        self.assertTrue(is_adult(18))

    def test_is_adult_false(self):
        self.assertFalse(is_adult(17))


if __name__ == "__main__":
    unittest.main()
```

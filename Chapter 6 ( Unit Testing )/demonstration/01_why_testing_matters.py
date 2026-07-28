"""Chapter 6 - Unit testing

This file introduces the idea of testing code to catch mistakes early.
"""

print("--- Why testing matters ---")


def add(a, b):
    return a + b


# A simple check using assert.
# If the result is wrong, Python will raise an AssertionError.
assert add(2, 3) == 5
assert add(-1, 1) == 0

print("Basic checks passed.")

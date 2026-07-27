"""Chapter 4 - Raising exceptions

This file shows how to raise an exception manually.
"""

print("--- Raising exceptions ---")


def check_temperature(temperature):
    if temperature < 0:
        raise ValueError("Temperature cannot be negative in this example.")
    return temperature


try:
    print(check_temperature(25))
    print(check_temperature(-5))
except ValueError as error:
    print("Error:", error)

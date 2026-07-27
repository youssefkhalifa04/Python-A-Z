"""Chapter 4 - Multiple exceptions

This file shows how to handle different errors.
"""

print("--- Multiple exceptions ---")

try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("Result:", a / b)
except ValueError:
    print("Please enter valid integers.")
except ZeroDivisionError:
    print("Division by zero is not allowed.")

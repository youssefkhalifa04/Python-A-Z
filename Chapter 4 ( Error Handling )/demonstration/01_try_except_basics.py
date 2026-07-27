"""Chapter 4 - Error handling

This file introduces try and except.
"""

print("--- Try / Except basics ---")

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)
except ValueError:
    print("That was not a valid integer.")

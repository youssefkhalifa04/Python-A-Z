"""Chapter 3 - Parameters and return values

This file shows functions with parameters and return values.
"""

print("--- Parameters and return values ---")


def square(number):
    return number * number


def full_name(first_name, last_name):
    return first_name + " " + last_name


result = square(5)
print("5 squared =", result)
print("Full name =", full_name("Sara", "Ali"))

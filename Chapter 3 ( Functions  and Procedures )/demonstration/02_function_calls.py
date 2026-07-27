"""Chapter 3 - Calling functions

This file shows how to pass arguments to functions.
"""

print("--- Function calls ---")


def greet(name):
    print("Hello", name)


def add(a, b):
    print("Sum:", a + b)

def multiply(x = 0, y = 0): # default parameters
    return x * y

greet("Amina")
greet("Karim")
add(4, 6)
add(10, 25)
print("Product:", multiply(3, 4))
print("Product with default values:", multiply())
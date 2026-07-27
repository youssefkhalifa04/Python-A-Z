"""Chapter 3 - Recursion

This file shows how a function can call itself.
"""

print("--- Recursion ---")


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print("factorial(5) =", factorial(5))
print("factorial(3) =", factorial(3))

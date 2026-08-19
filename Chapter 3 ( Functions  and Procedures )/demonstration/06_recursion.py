"""Chapter 3 - Recursion

This file shows how a function can call itself.
"""
'''
print("--- Recursion ---")


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print("factorial(5) =", factorial(5))
print("factorial(3) =", factorial(3))



def fact(number):
    value = 1
    for i in range (2, number+1):
        value = value * i
    return value

print("fact(5) =", fact(5))


'''


def a(n):
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1
        if c == 2 and i != n :
            return False
        if c == 2 and i == n:
            return True
print("a(9) =", a(9))

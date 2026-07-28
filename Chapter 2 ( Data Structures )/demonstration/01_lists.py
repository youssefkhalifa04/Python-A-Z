"""Chapter 2 - Lists

This file introduces Python lists and shows common list operations.
"""

print("--- Lists ---")

fruits = ["apple", "banana", "orange"]
print("Original list:", fruits)

fruits.append("mango")
print("After append:", fruits)

print("First item:", fruits[0])
print("Last item:", fruits[-1])

fruits[1] = "pear"
print("After replacement:", fruits)

print("Number of items:", len(fruits))

# Shallow copy
shallow_copy = fruits.copy()
shallow_copy.append("grape")
print("Original list after shallow copy append:", fruits)
print("Shallow copy list:", shallow_copy)

# Deep copy with nested list example
nested = [[1, 2], [3, 4]]
deep_copy = [item[:] for item in nested]
deep_copy[0][0] = 99
print("Original nested list:", nested)
print("Deep copy nested list:", deep_copy)

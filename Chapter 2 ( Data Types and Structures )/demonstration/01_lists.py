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

"""Chapter 2 - Sequences

A sequence is an ordered collection of items.
In Python, lists, tuples, and strings are common sequences.
"""

print("--- Sequences ---")

numbers = [10, 20, 30, 40]
text = "Python"

print("List is a sequence:", numbers)
print("String is also a sequence:", text)

print("Slicing a list:", numbers[1:3])
print("Slicing a string:", text[0:3])

print("Iterating over a sequence:")
for item in numbers:
    print(item)



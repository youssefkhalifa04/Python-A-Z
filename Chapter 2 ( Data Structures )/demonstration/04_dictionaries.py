"""Chapter 2 - Dictionaries

This file introduces dictionaries, which store key-value pairs.
"""

print("--- Dictionaries ---")

student = {
    "name": "Sara",
    "age": 21,
    "city": "Rabat",
}

print("Student dictionary:", student)
print("Name:", student["name"])
print("Age:", student["age"])

student["age"] = 22
student["grade"] = "A"

print("Updated dictionary:", student)
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))

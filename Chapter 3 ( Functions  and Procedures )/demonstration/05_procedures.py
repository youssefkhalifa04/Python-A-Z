"""Chapter 3 - Procedures

A procedure is a function that performs an action and does not return a value.
"""

print("--- Procedures ---")


def print_separator():
    print("-" * 30)


def display_student(name, age):
    print(f"Student: {name}")
    print(f"Age: {age}")
    print_separator()


display_student("Nora", 19)
display_student("Omar", 21)

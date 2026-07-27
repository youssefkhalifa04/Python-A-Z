"""Chapter 4 - else and finally

This file shows how else and finally work with try/except.
"""

print("--- Else and finally ---")

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid age.")
else:
    print("Your age is:", age)
finally:
    print("This message is always displayed.")

"""Chapter 4 - Practical example

This file combines input validation and cleanup.
"""

print("--- Practical example ---")

file_opened = False

try:
    numerator = int(input("Enter a numerator: "))
    denominator = int(input("Enter a denominator: "))
    result = numerator / denominator
    file_opened = True
    print("Result:", result)
except ValueError:
    print("Both values must be integers.")
except ZeroDivisionError:
    print("Denominator cannot be zero.")
finally:
    if file_opened:
        print("Cleanup step completed.")
    print("Program finished.")

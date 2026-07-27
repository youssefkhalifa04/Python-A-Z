# Correction - Chapter 4 Exercises

## Exercise 1 - Basic try/except
```python
try:
    number = int(input("Enter a number: "))
    print("Valid number:", number)
except ValueError:
    print("Invalid input. Please enter an integer.")
```

## Exercise 2 - finally and custom errors
```python
def check_positive(number):
    if number < 0:
        raise ValueError("The number must be positive.")
    return number


try:
    value = int(input("Enter a number: "))
    print(check_positive(value))
except ValueError as error:
    print("Error:", error)
finally:
    print("Cleanup is always executed.")
```

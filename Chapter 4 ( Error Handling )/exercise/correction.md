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

## Exercise 3 - Creating custom exceptions
```python
class InvalidPasswordError(Exception):
    pass


def validate_password(password):
    if len(password) < 8:
        raise InvalidPasswordError("Password must be at least 8 characters long.")
    
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    
    if not has_digit:
        raise InvalidPasswordError("Password must contain at least one digit.")
    
    return True


try:
    password = input("Enter a password: ")
    validate_password(password)
    print("Password is valid!")
except InvalidPasswordError as error:
    print(f"Password error: {error}")
```

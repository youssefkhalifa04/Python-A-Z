# Correction - Chapter 3 Exercises

## Exercise 1 - Basic functions
```python
def greet(name):
    print(f"Welcome, {name}!")


def rectangle_area(length, width):
    return length * width


greet("Amina")
area = rectangle_area(5, 3)
print("Area:", area)
```

## Exercise 2 - Global variables and procedures
```python
total_visits = 0


def add_visit():
    global total_visits
    total_visits += 1


def show_visits():
    print("Total visits:", total_visits)


add_visit()
add_visit()
add_visit()
show_visits()
```

## Exercise 3 - Recursion
```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


print("factorial(5) =", factorial(5))
print("factorial(3) =", factorial(3))
```

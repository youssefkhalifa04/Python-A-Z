# Correction - Chapter 2 Exercises

## Exercise 1 - Lists, tuples, and sequences
```python
colors = ["red", "blue", "green", "yellow"]
colors.append("purple")

print("First:", colors[0])
print("Last:", colors[-1])

point = (10, 20)
print("Point:", point)
print("Slice from list:", colors[1:3])
print("Slice from tuple:", point[:1])
```

## Exercise 2 - Dictionaries and sets
```python
student = {
    "name": "Lina",
    "age": 19,
    "course": "Python",
}

student["age"] = 20
student["city"] = "Tunis"

print(student)

values = {1, 2, 2, 3, 3, 4}
print(values)

other_values = {3, 4, 5}
print("Union:", values | other_values)
print("Intersection:", values & other_values)
```

## Exercise 3 - Palindrome
### Built-in style
```python
text = input("Enter a string: ")

if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
```

### Beginner style
```python
text = input("Enter a string: ")
reversed_text = ""

for character in text:
    reversed_text = character + reversed_text

if text == reversed_text:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
```

## Exercise 4 - Minimum value in a list
### Built-in style
```python
numbers = [18, 4, 27, 9, 12]

smallest = min(numbers)
print("The smallest number is:", smallest)
```

### Beginner style
```python
numbers = [18, 4, 27, 9, 12]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("The smallest number is:", smallest)
```

## Exercise 5 - Divisors of a number
### Built-in style
```python
number = int(input("Enter a positive number: "))

divisors = [divisor for divisor in range(1, number + 1) if number % divisor == 0]
print("Divisors:", divisors)
```

### Beginner style
```python
number = int(input("Enter a positive number: "))

print("Divisors:")

divisor = 1
while divisor <= number:
    if number % divisor == 0:
        print(divisor)
    divisor += 1
```

## Exercise 6 - Digits only
### Built-in style
```python
text = input("Enter a string: ")

if text.isdigit():
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")
```

### Beginner style
```python
text = input("Enter a string: ")

only_digits = True

for character in text:
    if character < "0" or character > "9":
        only_digits = False
        break

if only_digits and text != "":
    print("The string contains only digits.")
else:
    print("The string does not contain only digits.")
```

## Exercise 7 - Inventory analysis
### Built-in style
```python
products = [
    {"name": "Pen", "category": "Stationery", "price": 1.5, "quantity": 20},
    {"name": "Notebook", "category": "Stationery", "price": 3.0, "quantity": 15},
    {"name": "Mouse", "category": "Electronics", "price": 25.0, "quantity": 5},
    {"name": "Keyboard", "category": "Electronics", "price": 40.0, "quantity": 3},
]

total_value = sum(product["price"] * product["quantity"] for product in products)
most_expensive = max(products, key=lambda product: product["price"])
categories = {product["category"] for product in products}

category_quantities = {}
for product in products:
    category = product["category"]
    category_quantities[category] = category_quantities.get(category, 0) + product["quantity"]

print("Total inventory value:", total_value)
print("Most expensive product:", most_expensive["name"])
print("Unique categories:", categories)
print("Category quantities:", category_quantities)
```

### Beginner style
```python
products = [
    {"name": "Pen", "category": "Stationery", "price": 1.5, "quantity": 20},
    {"name": "Notebook", "category": "Stationery", "price": 3.0, "quantity": 15},
    {"name": "Mouse", "category": "Electronics", "price": 25.0, "quantity": 5},
    {"name": "Keyboard", "category": "Electronics", "price": 40.0, "quantity": 3},
]

total_value = 0
most_expensive_product = products[0]
categories = []
category_quantities = {}

for product in products:
    total_value += product["price"] * product["quantity"]

    if product["price"] > most_expensive_product["price"]:
        most_expensive_product = product

    if product["category"] not in categories:
        categories.append(product["category"])

    category = product["category"]
    if category in category_quantities:
        category_quantities[category] += product["quantity"]
    else:
        category_quantities[category] = product["quantity"]

print("Total inventory value:", total_value)
print("Most expensive product:", most_expensive_product["name"])
print("Unique categories:", categories)
print("Category quantities:", category_quantities)
```

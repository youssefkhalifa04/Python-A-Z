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

---

## Exercise 4 - Shopping Cart System

```python
def add_item(cart, name, price, quantity=1):
    for item in cart:
        if item["name"] == name:
            item["quantity"] += quantity
            return
    cart.append({"name": name, "price": price, "quantity": quantity})


def remove_item(cart, name):
    for i, item in enumerate(cart):
        if item["name"] == name:
            cart.pop(i)
            return
    print(f"Item '{name}' not found in cart.")


def apply_discount(cart, percent):
    for item in cart:
        item["price"] *= (1 - percent / 100)


def calculate_total(cart):
    return sum(item["price"] * item["quantity"] for item in cart)


def print_receipt(cart):
    print("----- RECEIPT -----")
    for item in cart:
        line_total = item["price"] * item["quantity"]
        print(f"  {item['name']} x{item['quantity']}  ->  {line_total:.2f} DH")
    print(f"  TOTAL: {calculate_total(cart):.2f} DH")
    print("-------------------")


# Test
cart = []
add_item(cart, "Apple", 5.0, 3)
add_item(cart, "Bread", 12.0)
add_item(cart, "Milk", 8.5)
add_item(cart, "Apple", 5.0, 2)  # increases quantity
remove_item(cart, "Milk")
apply_discount(cart, 10)
print_receipt(cart)
```

## Exercise 5 - Student Grade Manager

```python
def average(grades):
    return sum(grades) / len(grades)


def letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def class_report(students):
    print("===== CLASS REPORT =====")
    for name, grades in students.items():
        avg = average(grades)
        lg = letter_grade(avg)
        print(f"  {name}: avg={avg:.1f} -> {lg}")
    print("========================")


def top_students(students):
    return [name for name, grades in students.items() if average(grades) >= 80]


def pass_rate(students):
    passed = sum(1 for grades in students.values() if average(grades) >= 60)
    return (passed / len(students)) * 100


# Test
students = {
    "Alice": [92, 88, 95],
    "Bob": [70, 65, 72],
    "Charlie": [55, 48, 60],
    "Diana": [85, 90, 88],
}
class_report(students)
print("Top students:", top_students(students))
print(f"Pass rate: {pass_rate(students):.1f}%")
```

## Exercise 6 - Text Analysis Tool

```python
def count_words(text):
    return len(text.split())


def count_vowels(text):
    return sum(1 for ch in text.lower() if ch in "aeiou")


def longest_word(text):
    words = text.split()
    return max(words, key=len)


def word_frequency(text):
    freq = {}
    for word in text.lower().split():
        freq[word] = freq.get(word, 0) + 1
    return freq


def replace_word(text, old, new):
    return text.replace(old, new)
# another method
def replace_word(text, old, new):
    words = text.split(' ')
    for i in range(len(words)):
        if words[i] == old:
            words[i] = new

    return ' '.join(words)

# Test
sample = "the cat sat on the mat and the cat liked the mat"
print("Word count:", count_words(sample))
print("Vowel count:", count_vowels(sample))
print("Longest word:", longest_word(sample))
print("Word frequency:", word_frequency(sample))
print("Replace:", replace_word(sample, "cat", "dog"))
```

## Exercise 7 - Number Sequence Analyzer

```python
def is_arithmetic(sequence):
    if len(sequence) < 2:
        return True
    diff = sequence[1] - sequence[0]
    return all(sequence[i] - sequence[i - 1] == diff for i in range(2, len(sequence)))


def is_geometric(sequence):
    if len(sequence) < 2:
        return True
    if sequence[0] == 0:
        return False
    ratio = sequence[1] / sequence[0]
    return all(sequence[i] / sequence[i - 1] == ratio for i in range(2, len(sequence)))


def next_arithmetic(sequence):
    diff = sequence[-1] - sequence[-2]
    return sequence[-1] + diff


def next_geometric(sequence):
    ratio = sequence[-1] / sequence[-2]
    return sequence[-1] * ratio


def series_sum(gen_func, n):
    return sum(gen_func(i) for i in range(n))


# Test
arith = [2, 5, 8, 11]
geo = [3, 6, 12, 24]
print("Arithmetic:", is_arithmetic(arith), "-> next:", next_arithmetic(arith))
print("Geometric:", is_geometric(geo), "-> next:", next_geometric(geo))

# Alternative approach using only loops (no all/ generator)
def is_arithmetic_v2(sequence):
    if len(sequence) < 2:
        return True
    diff = sequence[1] - sequence[0]
    for i in range(2, len(sequence)):
        if sequence[i] - sequence[i - 1] != diff:
            return False
    return True
```

## Exercise 8 - Bank Account Simulator

```python
def create_account(owner, balance=0):
    return {"owner": owner, "balance": balance, "transactions": []}


def deposit(account, amount):
    account["balance"] += amount
    account["transactions"].append(f"+{amount:.2f}")


def withdraw(account, amount):
    if amount > account["balance"]:
        print(f"Error: insufficient funds for {account['owner']} (has {account['balance']:.2f})")
        return False
    account["balance"] -= amount
    account["transactions"].append(f"-{amount:.2f}")
    return True


def transfer(sender, receiver, amount):
    if withdraw(sender, amount):
        deposit(receiver, amount)
        print(f"Transferred {amount:.2f} from {sender['owner']} to {receiver['owner']}")


def add_interest(account, rate):
    interest = account["balance"] * rate / 100
    account["balance"] += interest
    account["transactions"].append(f"+{interest:.2f} (interest)")


def print_statement(account):
    print(f"===== Statement for {account['owner']} =====")
    for t in account["transactions"]:
        print(f"  {t}")
    print(f"  Balance: {account['balance']:.2f}")
    print("===========================================")


# Test
alice = create_account("Alice", 1000)
bob = create_account("Bob", 500)
deposit(alice, 200)
withdraw(alice, 150)
transfer(alice, bob, 300)
add_interest(bob, 5)
print_statement(alice)
print_statement(bob)
```

## Exercise 9 - Dice Roll Statistics

```python
import random


def roll_dice(sides=6):
    return random.randint(1, sides)


def roll_multiple(n, sides=6):
    return [roll_dice(sides) for _ in range(n)]


def roll_stats(n, sides=6):
    rolls = roll_multiple(n, sides)
    freq = {}
    for r in rolls:
        freq[r] = freq.get(r, 0) + 1
    return {
        "total": sum(rolls),
        "average": sum(rolls) / len(rolls),
        "min": min(rolls),
        "max": max(rolls),
        "frequency": freq,
    }


def roll_until(target, sides=6):
    count = 0
    while True:
        count += 1
        if roll_dice(sides) == target:
            return count


def lucky_sevens(n, sides=6):
    count = 0
    for _ in range(n):
        d1 = roll_dice(sides)
        d2 = roll_dice(sides)
        if d1 + d2 == 7:
            count += 1
    return count


# Alternative using filter (functional style)
def lucky_sevens_v2(n, sides=6):
    rolls = [(roll_dice(sides), roll_dice(sides)) for _ in range(n)]
    return len(list(filter(lambda pair: pair[0] + pair[1] == 7, rolls)))


# Test
random.seed(42)
stats = roll_stats(1000)
print("Stats:", stats)
print("Rolls until 6:", roll_until(6))
print("Lucky 7s in 1000 rolls:", lucky_sevens(1000))
```

## Exercise 10 - Palindrome and Word Play

```python
def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def reverse_words(text):
    return " ".join(text.split()[::-1])


def count_letters(text):
    freq = {}
    for ch in text.lower():
        if ch.isalpha():
            freq[ch] = freq.get(ch, 0) + 1
    return freq


def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())


def caesar_cipher(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            shifted = (ord(ch) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(ch)
    return "".join(result)


# Alternative is_anagram using Counter
from collections import Counter

def is_anagram_v2(word1, word2):
    return Counter(word1.lower()) == Counter(word2.lower())


# Test
print(is_palindrome("Racecar"))
print(is_palindrome("hello"))
print(reverse_words("hello world"))
print(count_letters("Hello World"))
print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))
print(caesar_cipher("Hello World", 3))
print(caesar_cipher("Khoor Zruog", -3))  # decrypt
```

## Exercise 11 - Higher-Order Functions and Lambdas

```python
from functools import reduce

products = [
    {"name": "Laptop", "price": 25000, "category": "Electronics"},
    {"name": "Phone", "price": 15000, "category": "Electronics"},
    {"name": "Shirt", "price": 300, "category": "Clothing"},
    {"name": "Pants", "price": 500, "category": "Clothing"},
    {"name": "Book", "price": 120, "category": "Education"},
]

# Sort by price ascending
by_price = sorted(products, key=lambda p: p["price"])
print("By price:", [p["name"] for p in by_price])

# Sort by name
by_name = sorted(products, key=lambda p: p["name"])
print("By name:", [p["name"] for p in by_name])

# Filter under 1000
cheap = list(filter(lambda p: p["price"] < 1000, products))
print("Cheap:", [p["name"] for p in cheap])

# Map to names only
names = list(map(lambda p: p["name"], products))
print("Names:", names)


def group_by_category(products):
    groups = {}
    for p in products:
        cat = p["category"]
        if cat not in groups:
            groups[cat] = []
        groups[cat].append(p)
    return groups


# Alternative using reduce
def group_by_category_v2(products):
    return reduce(
        lambda acc, p: {**acc, p["category"]: acc.get(p["category"], []) + [p]},
        products,
        {},
    )


def apply_to_all(items, func):
    return [func(item) for item in items]


# Test
print("Grouped:", group_by_category(products))
print("Doubled:", apply_to_all([1, 2, 3, 4], lambda x: x * 2))
```

## Exercise 12 - Decorators and Closures

```python
import time
from functools import wraps


def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[CALL] {func.__name__}({args}, {kwargs})")
        result = func(*args, **kwargs)
        print(f"[RETURN] {func.__name__} -> {result}")
        return result
    return wrapper


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"[TIMER] {func.__name__} took {elapsed:.4f}s")
        return result
    return wrapper


def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        print(f"Count: {count}")
        return count
    return increment


def power_factory(exponent):
    def power(base):
        return base ** exponent
    return power


@log_calls
def add(a, b):
    return a + b


@timer
def slow_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total


# Test
add(3, 5)
slow_sum(1000000)

my_counter = counter()
my_counter()
my_counter()
my_counter()

square = power_factory(2)
cube = power_factory(3)
print("5^2 =", square(5))
print("2^3 =", cube(2))
```

## Exercise 13 - Recursive Problems

```python
def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])


def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


def count_occurrences(lst, target):
    count = 0
    for item in lst:
        if isinstance(item, list):
            count += count_occurrences(item, target)
        elif item == target:
            count += 1
    return count


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Alternative flatten using list comprehension (more Pythonic)
def flatten_v2(nested_list):
    return [
        item
        for sublist in nested_list
        for item in (flatten_v2(sublist) if isinstance(sublist, list) else [sublist])
    ]


# Test
print("Sum:", sum_list([1, 2, 3, 4, 5]))
print("Flatten:", flatten([1, [2, 3], [4, [5, 6]], 7]))
print("Power:", power(2, 10))
print("Occurrences:", count_occurrences([1, [2, 1], [1, [1, 3]], 4], 1))
print("Fibonacci(10):", fibonacci(10))
```
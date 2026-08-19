# Chapter 3 - Exercises

This folder contains short exercises for the third chapter of the course.

## How to use
- Read the exercise statements in this file.
- Write your attempts in `attempts.py`.
- Check the correction in `correction.md` only after trying the exercises.

## Exercise 1 - Basic functions
1. Create a function named `greet` that takes a name and prints a welcome message.
2. Create a function named `rectangle_area` that takes `length` and `width` and returns the area.
3. Call both functions with example values.
4. Print the returned area.

## Exercise 2 - Global variables and procedures
1. Create a global variable named `total_visits` starting at `0`.
2. Create a function that increments `total_visits` using the `global` keyword.
3. Call the function three times.
4. Create a procedure that displays the current value of `total_visits`.

## Exercise 3 - Recursion
1. Create a recursive function named `factorial`.
2. Make it return `1` when the number is `0` or `1`.
3. Make it call itself for larger values.
4. Test it with at least two numbers.

---

## Exercise 4 - Shopping Cart System
Build a simple shopping cart using functions. The cart is a list of dictionaries, where each item has a `name`, `price`, and `quantity`.

1. Create a function `add_item(cart, name, price, quantity=1)` that adds an item to the cart. If the item already exists, increase its quantity.
2. Create a function `remove_item(cart, name)` that removes an item from the cart by name.
3. Create a function `apply_discount(cart, percent)` that reduces every item's price by the given percentage.
4. Create a function `calculate_total(cart)` that returns the total cost of all items.
5. Create a function `print_receipt(cart)` that displays each item and the final total.
6. Test the full flow: add items, apply a discount, print the receipt.

## Exercise 5 - Student Grade Manager
You have a dictionary where keys are student names and values are lists of numeric grades.

1. Create a function `average(grades)` that returns the mean of a list of numbers.
2. Create a function `letter_grade(avg)` that returns `"A"`, `"B"`, `"C"`, `"D"`, or `"F"` based on the average (90+, 80+, 70+, 60+, below 60).
3. Create a function `class_report(students)` that builds and prints a report: each student's name, average, and letter grade.
4. Create a function `top_students(students)` that returns a list of names of students whose average is 80 or above.
5. Create a function `pass_rate(students)` that returns the percentage of students who passed (average >= 60).
6. Test with at least 3 students with different grade lists.

## Exercise 6 - Text Analysis Tool
Write a set of functions to analyze a given text string.

1. Create a function `count_words(text)` that returns the number of words in the text.
2. Create a function `count_vowels(text)` that returns the count of vowels (a, e, i, o, u), case-insensitive.
3. Create a function `longest_word(text)` that returns the longest word in the text.
4. Create a function `word_frequency(text)` that returns a dictionary with each word as key and its count as value (case-insensitive).
5. Create a function `replace_word(text, old, new)` that replaces every occurrence of `old` with `new`.
6. Run the functions on a sample paragraph and print all results.

## Exercise 7 - Number Sequence Analyzer
Write functions to analyze and generate number sequences.

1. Create a function `is_arithmetic(sequence)` that returns `True` if the sequence has a constant difference between consecutive terms.
2. Create a function `is_geometric(sequence)` that returns `True` if the sequence has a constant ratio between consecutive terms.
3. Create a function `next_arithmetic(sequence)` that returns the next term in an arithmetic sequence.
4. Create a function `next_geometric(sequence)` that returns the next term in a geometric sequence.
5. Create a function `series_sum(sequence, n)` that returns the sum of the first `n` terms of any sequence given as a function.
6. Test with `[2, 5, 8, 11]` (arithmetic) and `[3, 6, 12, 24]` (geometric).

## Exercise 8 - Bank Account Simulator
Simulate a bank account using functions and a global account state.

1. Create a function `create_account(owner, balance=0)` that initializes an account dictionary with `owner`, `balance`, and a `transactions` list.
2. Create a function `deposit(account, amount)` that adds to the balance and logs the transaction.
3. Create a function `withdraw(account, amount)` that subtracts from the balance (only if sufficient funds) and logs the transaction. Print an error if funds are insufficient.
4. Create a function `transfer(sender, receiver, amount)` that moves money between two accounts.
5. Create a function `add_interest(account, rate)` that adds interest (balance * rate / 100) to the account.
6. Create a function `print_statement(account)` that prints all transactions and the current balance.
7. Test with two accounts, perform deposits, withdrawals, a transfer, and add interest.

## Exercise 9 - Dice Roll Statistics
Simulate rolling dice and compute statistics using functions.

1. Create a function `roll_dice(sides=6)` that returns a random integer between 1 and `sides`.
2. Create a function `roll_multiple(n, sides=6)` that returns a list of `n` dice rolls.
3. Create a function `roll_stats(n, sides=6)` that returns a dictionary with keys `"total"`, `"average"`, `"min"`, `"max"`, and `"frequency"` (a dict of each face and how many times it appeared).
4. Create a function `roll_until(target, sides=6)` that rolls repeatedly until `target` appears and returns the number of rolls needed.
5. Create a function `lucky_sevens(n, sides=6)` that counts how many rolls out of `n` resulted in a 7 (use two dice, `sides=6`).
6. Run the functions and display all results.

## Exercise 10 - Palindrome and Word Play
Write a set of functions for word manipulation and puzzles.

1. Create a function `is_palindrome(text)` that returns `True` if the text reads the same forwards and backwards (ignore spaces and case).
2. Create a function `reverse_words(text)` that reverses the order of words in a string.
3. Create a function `count_letters(text)` that returns a dictionary of each letter and its frequency (case-insensitive, ignore non-letters).
4. Create a function `is_anagram(word1, word2)` that returns `True` if both words are anagrams of each other.
5. Create a function `caesar_cipher(text, shift)` that encrypts text by shifting each letter by `shift` positions in the alphabet.
6. Test with sample inputs like `"racecar"`, `"hello world"`, `"listen"` and `"silent"`.

## Exercise 11 - Higher-Order Functions and Lambdas
Practice using functions as values, lambda expressions, and built-in higher-order functions.

1. Create a list of dictionaries representing products: `{"name": "...", "price": ..., "category": "..."}`.
2. Use `sorted()` with a `lambda` to sort products by price ascending.
3. Use `sorted()` with a `lambda` to sort products by name alphabetically.
4. Use `filter()` with a `lambda` to get only products under a given price.
5. Use `map()` with a `lambda` to create a new list of just the product names.
6. Create a function `group_by_category(products)` that returns a dictionary where keys are categories and values are lists of products in that category. Use a loop or `functools.reduce`.
7. Create a function `apply_to_all(items, func)` that applies `func` to every element and returns the new list. Call it with a lambda that doubles numeric values.

## Exercise 12 - Decorators and Closures
Practice defining and using decorators and closures.

1. Create a decorator `log_calls(func)` that prints the function name and its arguments every time the decorated function is called.
2. Create a decorator `timer(func)` that prints how long the function took to execute (use `time` module).
3. Create a function `counter()` that returns a closure. Each call to the returned function increments and prints a count starting from 0.
4. Create a function `power_factory(exponent)` that returns a closure. The closure raises its argument to the given exponent.
5. Apply `@log_calls` to a function `add(a, b)` and test it.
6. Apply `@timer` to a function `slow_sum(n)` that sums numbers from 0 to `n` using a loop, and test it.

## Exercise 13 - Recursive Problems
Solve these problems using recursion (no loops allowed inside the recursive functions).

1. Create a function `sum_list(lst)` that returns the sum of all elements in a list using recursion.
2. Create a function `flatten(nested_list)` that takes a list that may contain nested lists and returns a single flat list.
3. Create a function `power(base, exp)` that computes `base ** exp` using recursion (handle `exp = 0` as base case).
4. Create a function `count_occurrences(lst, target)` that counts how many times `target` appears in `lst`, including in nested sublists.
5. Create a function `fibonacci(n)` that returns the `n`-th Fibonacci number using recursion (n=0 returns 0, n=1 returns 1).
6. Test all functions with sample inputs.

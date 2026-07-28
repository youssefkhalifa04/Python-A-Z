# Chapter 4 FAQ

## Beginner questions

### What is error handling?
Error handling allows your program to deal with problems without crashing.

### Why do we need error handling?
We need it because user input and external data can be unexpected.

### What does `try` do?
`try` contains the code that may fail.

### What is the use of `except`?
`except` runs when an error happens in the `try` block.

### When should I use `except`?
Use `except` whenever you want to recover from an error instead of stopping the program.

## Intermediate questions

### When should I use `finally`?
Use `finally` for cleanup code that must run whether an error happens or not.

### What is the difference between `ValueError` and `ZeroDivisionError`?
`ValueError` is raised for invalid values, while `ZeroDivisionError` happens when dividing by zero.

### Why is it better to handle errors than to let the program crash?
Handled errors create a better user experience and make programs more robust.

## Advanced questions

### How do I design error handling for real applications?
Catch specific exceptions, show helpful messages, and keep the program in a safe state.

### Why is it important to avoid catching everything blindly?
Catching every exception can hide real bugs and make debugging harder.

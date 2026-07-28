# Chapter 6 FAQ

## Beginner questions

### What is unit testing?
Unit testing checks whether a small part of the program works correctly.

### Why should I test my code?
Testing helps catch mistakes early and makes code easier to maintain.

### When should I write tests?
Write tests whenever you create or change important logic, especially functions that may be reused.

### What is `assert`?
`assert` checks whether a condition is true and raises an error if it is not.

## Intermediate questions

### What is the difference between `assert` and `unittest`?
`assert` is simple and useful for quick checks, while `unittest` provides a structured testing framework.

### Why use `setUp` and `tearDown`?
They help prepare test data before each test and clean it up afterward.

### Why do we test one behavior at a time?
Testing one behavior at a time makes failures easier to understand and fix.

## Advanced questions

### Why is testing important in larger projects?
In larger projects, tests prevent regressions and make collaboration safer.

### How do tests help with refactoring?
Tests give you confidence that changes did not break existing behavior.

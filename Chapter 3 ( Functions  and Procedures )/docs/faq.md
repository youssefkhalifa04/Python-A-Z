# Chapter 3 FAQ

## Beginner questions

### What is a function?
A function is a reusable block of code that performs a specific task.

### Why do we use functions?
We use functions to avoid repeating code and to organize programs better.

### What is the difference between a function and a procedure?
A function usually returns a value, while a procedure mainly performs an action.

### What is a parameter?
A parameter is a value passed into a function.

### When should I use a function?
Use a function whenever you need to perform the same action several times or split a task into smaller parts.

## Intermediate questions

### Why use `global` carefully?
`global` lets a function change a variable outside its own scope, but it can make code harder to understand.

### What is recursion?
Recursion happens when a function calls itself to solve a smaller version of the same problem.

### When is recursion a good idea?
Recursion is useful for problems that naturally break into smaller versions of the same problem, such as factorials or tree traversal.

### Why should functions return values instead of just printing?
Returning values makes functions more reusable and easier to combine with other code.

## Advanced questions

### How do functions help with maintainability?
Functions make code easier to test, modify, and understand because each function has a clear responsibility.

### What is the downside of overusing global variables?
Too many global variables can make programs harder to debug and reason about because state is shared everywhere.

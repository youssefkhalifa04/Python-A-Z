"""Chapter 3 - Global and local variables

This file explains the difference between local and global variables.
"""

print("--- Global and local variables ---")

counter = 0


def increment_counter():
    global counter
    counter += 1
    print("Counter inside the function:", counter)


def show_local_variable():
    message = "This variable exists only inside the function"
    print(message)


increment_counter()
increment_counter()
show_local_variable()
print("Counter outside the function:", counter)
#print (message)  # This will raise an error because 'message' is a local variable
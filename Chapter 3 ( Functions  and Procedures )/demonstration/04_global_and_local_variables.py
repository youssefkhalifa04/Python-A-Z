"""Chapter 3 - Global and local variables

This file explains the difference between local and global variables.
"""



counter = 0




def show_local_variable():
    global counter
    message = "This variable exists only inside the function"
    print(message)
    counter + = 1
   
    print("Counter inside the function:", counter)
    
def newfunction():
    a = counter 
    a += 1
    return a 


counter  = newfunction()




b = show_local_variable()

#print (message)  # This will raise an error because 'message' is a local variable
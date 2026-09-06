a=input("write a number")
try:
    a = int(a)
    print("You entered:", a)
    print(a, "was really an integer !")
except ValueError:
    print("That was not a valid integer.")

def num(a):
    if a<0:
        raise ValueError("a is negative")
    else : 
        return a 
try:
    num(1)
except ValueError as e:
    print(e)
finally:
    print("good work")



class InvalidPasswordError (Exception):
    pass
def validate_password(a):
    if len(a)<8 :
        raise InvalidPasswordError("password must be longer then 8 chars")   
    counter = 0
    for i in a :
        if isnum(i) : 
            counter += 1
            break
    if counter < 0 :
        raise InvalidPasswordError("password must contain at least one number")



try:
     
    validate_password("gtrgdhdthd")
except InvalidPasswordError as p:
    print(p)
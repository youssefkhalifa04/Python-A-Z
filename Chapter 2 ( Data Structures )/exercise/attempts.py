'''
number = 0 
print("Enter a positive number: ")
number = int(input())
while number < 0 :
    print("The number is negative")
    print("Enter a positive number: ")
    number = int(input())

print("number : ", number)'''



'''number = 0

while True : 
    print("Enter a positive number: ")
    number = int(input())
    if number < 0 :
        print("The number is negative")
    else:
        break

print("number : ", number)


l = []
for i in range (1, number//2 + 1) : 
    
    if number % i == 0 :
        l.append(i)


print('les diviseurs de ', number, ' sont : ', end = " ")
for i in l:
    print(i, end = " ")
  '''


'''
number = input("Enter a positive number: ")
a = "1255"
        
counter = 0 
for i in number :
    if i  in '0123456789' :
         print("i : ", i)
    counter += 1 

print("counter : ", counter)
print("len(number) - 1: ", len(number)-1)       
'''

number = input("Enter a positive number: ")
if number.isdigit() :
    print("the number contains only digits")
else :
    print("the number contains non-digit characters")




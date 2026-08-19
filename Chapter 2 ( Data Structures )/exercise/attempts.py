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

'''number = input("Enter a positive number: ")
if number.isdigit() :
    print("the number contains only digits")
else :
    print("the number contains non-digit characters")
'''

l = [
    {
        "name" : "chlaka",
        "price" : 20,
        "quantity" : 5,
        "category" : "clothing"
    },
    {
        "name" : "sabbat",
        "price" : 90,
        "quantity" : 5,
        "category" : "clothing"
    },
    {
        "name" : "serwel",
        "price" : 80,
        "quantity" : 15,
        "category" : "clothing"
    },
    {
        "name" : "souriya",
        "price" : 40,
        "quantity" : 55,
        "category" : "clothing"
    },
    {
        "name" : "maryoul",
        "price" : 35,
        "quantity" : 50,
        "category" : "clothing"
    },
    {
        "name" : "kaskrout chawrma",
        "price" : 100,
        "quantity" : 20,
        "category" : "food"
    }
]


'''total_value = 0
for product in l :
    s = product["price"] * product["quantity"]
    total_value = total_value + s

print("Total value of inventory: ", total_value)'''





'''
most_expensive_product = max(l, key=lambda x: x["quantity"])

print("Most quantity product: ", most_expensive_product["name"])'''
'''
most_expensive_product = l[0]

for product in l :
    if product["price"] > most_expensive_product["price"] :
        most_expensive_product = product

print("Most expensive product: ", most_expensive_product["name"])'''



'''# 1. Display all unique categories.
unique_categories = set(product["category"] for product in l)
print("Unique categories: ", unique_categories)'''



#1. Calculate the total quantity for each category. (group by)

'''
from itertools import groupby
grouped = groupby(l, key=lambda x: x["category"])
for category, products in grouped:
    total_quantity = sum(product["quantity"] for product in products)
    print(f"Total quantity for {category}: {total_quantity}")
'''
D = {}

for product in l:
    D[product["category"]] = D.get(product["category"], 0) + product["quantity"]



print("Total quantity for each category: ", D)
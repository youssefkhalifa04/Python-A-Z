"""Les structures itératives en Python.

Ce fichier montre une boucle for et une boucle while.
"""

print("--- Structures itératives ---")

print("Boucle for :")
for i in range(1, 6):
    print("i =", i)


ch = "bonjour"

for i in ch :
    print(i+"\n")


dic = {"nom": "Dupont", "age": 30, "ville": "Paris"}

for key , value in dic.items():
    print(key, ":", value)

for key in dic.keys():
    print(key)
for value in dic.values():
    print(value)



c = 0
while True:
    print("boucle while true")
    c += 1
    if c >= 5:
        break
while c < 5:
    print("boucle while c < 5")
    c += 1




print("Boucle while :")
compteur = 0
while compteur < 3:
    print("compteur =", compteur)
    compteur += 1





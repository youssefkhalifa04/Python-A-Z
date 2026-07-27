# Correction - Chapter 1 Exercises

## Exercise 1 - Variables, types, input/output
```python
prenom = "Amina"
age = 20

print(f"Je m'appelle {prenom} et j'ai {age} ans.")

ville = input("Quelle est ta ville préférée ? ")
print("Ta ville préférée est :", ville)
```

## Exercise 2 - Operators and control flow
```python
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

print("Somme :", nombre1 + nombre2)
print("Différence :", nombre1 - nombre2)
print("Produit :", nombre1 * nombre2)
print("Quotient :", nombre1 / nombre2)

note = float(input("Entrez une note : "))

if note >= 16:
    print("Très bien")
elif note >= 10:
    print("Passable")
else:
    print("Insuffisant")

for i in range(1, 6):
    print(i)
```

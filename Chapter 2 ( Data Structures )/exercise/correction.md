# Correction - Chapter 2 Exercises

## Exercise 1 - Lists, tuples, and sequences
```python
colors = ["red", "blue", "green", "yellow"]
colors.append("purple")

print("First:", colors[0])
print("Last:", colors[-1])

point = (10, 20)
print("Point:", point)
print("Slice from list:", colors[1:3])
print("Slice from tuple:", point[:1])
```

## Exercise 2 - Dictionaries and sets
```python
student = {
    "name": "Lina",
    "age": 19,
    "course": "Python",
}

student["age"] = 20
student["city"] = "Tunis"

print(student)

values = {1, 2, 2, 3, 3, 4}
print(values)

other_values = {3, 4, 5}
print("Union:", values | other_values)
print("Intersection:", values & other_values)
```

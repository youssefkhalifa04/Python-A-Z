


def test(a):
    if a > 0:
        return "Positive"
    else : 
        return None

print(test(5))  # Positive
print(test(-3))  # None



student1 = {
    "name": "John",
    "age": 20,
    "major": "Computer Science",
    "grades": [90, 85, 78],
    "subjects" : ["Math", "Physics", "Chemistry"]
}

student = {
    "name": "John",
    "age": 20,
    "major": "Computer Science",
    "grades": {
        "math": 90,
        "science": 85,
        "history": 78
    }
}


print(student["grades"]["math"])  # 90

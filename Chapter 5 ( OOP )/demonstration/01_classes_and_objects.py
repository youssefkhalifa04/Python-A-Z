"""Chapter 5 - Classes and objects

This file introduces the class-object relationship.
"""

print("--- Classes and objects ---")


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")


student1 = Student("Amina", 20)
student2 = Student("Karim", 22)

student1.introduce()
student2.introduce()

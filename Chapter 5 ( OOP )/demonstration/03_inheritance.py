"""Chapter 5 - Inheritance

This file shows how a child class reuses and extends a parent class.
"""

print("--- Inheritance ---")


class Person:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"Hello, I am {self.name}.")


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def speak(self):
        print(f"Hello, I am {self.name} and I teach {self.subject}.")

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def speak(self):
        print(f"Hello, I am {self.name} and my grade is {self.grade}.")

person = Person("Nora")
teacher = Teacher("Omar", "Python")
student = Student("Amina", 10)

person.speak()
teacher.speak()
student.speak()

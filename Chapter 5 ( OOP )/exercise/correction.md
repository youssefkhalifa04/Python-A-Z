# Correction - Chapter 5 Exercises

## Exercise 1 - Classes and objects
```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def show_info(self):
        print(f"{self.title} by {self.author} - {self.pages} pages")


book1 = Book("Python Basics", "Alice", 180)
book2 = Book("OOP Guide", "Bob", 220)

book1.show_info()
book2.show_info()
```

## Exercise 2 - Inheritance and polymorphism
```python
class Animal:
    def sound(self):
        print("Some sound")


class Dog(Animal):
    def sound(self):
        print("Woof")


class Cat(Animal):
    def sound(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
```

## Exercise 3 - Abstract classes
```python
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print("The car is driving")


class Bike(Vehicle):
    def move(self):
        print("The bike is moving")


car = Car()
bike = Bike()

car.move()
bike.move()
```

## Exercise 4 - Encapsulation
```python
class Student:
    def __init__(self, name, section, grade):
        self.name = name
        self._section = section
        self.__grade = grade

    def show_grade(self):
        print(f"{self.name}'s grade: {self.__grade}")


student = Student("Lina", "A", 18)
print(student.name)
print(student._section)
student.show_grade()
```

## Exercise 5 - Interfaces and polymorphism
```python
from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} by card")


class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} in cash")


payments = [CardPayment(), CashPayment()]

for payment in payments:
    payment.pay(20)
```

## Exercise 6 - Composition
```python
class Address:
    def __init__(self, city, country):
        self.city = city
        self.country = country


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def show_profile(self):
        print(f"Name: {self.name}")
        print(f"City: {self.address.city}")
        print(f"Country: {self.address.country}")


address = Address("Tunis", "Tunisia")
person = Person("Sara", address)
person.show_profile()
```

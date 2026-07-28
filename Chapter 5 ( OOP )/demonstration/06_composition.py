"""Chapter 5 - Composition

This file shows composition, where a class uses another class as a component.
It is a good alternative to inheritance when objects should contain behavior.
"""

print("--- Composition ---")


class Address:
    def __init__(self, city, country):
        self.city = city
        self.country = country

    def show(self):
        print(f"City: {self.city}, Country: {self.country}")


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def show_profile(self):
        print(f"Name: {self.name}")
        self.address.show()


address = Address("Tunis", "Tunisia")
person = Person("Sara", address)

person.show_profile()

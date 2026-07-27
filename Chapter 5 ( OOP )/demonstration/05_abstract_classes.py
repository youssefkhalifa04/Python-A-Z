"""Chapter 5 - Abstract classes

This file shows how an abstract class defines a common contract.
"""

from abc import ABC, abstractmethod

print("--- Abstract classes ---")


class Shape(ABC): # an abstract class cannot be instantiated
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius * self.radius


rectangle = Rectangle(4, 5)
circle = Circle(3)

print("Rectangle area:", rectangle.area())
print("Circle area:", circle.area())

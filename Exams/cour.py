from abc import ABC, abstractmethod


class Shape(ABC) :
    __name : str
    @abstractmethod
    def calc_area(self):
        pass

    def get_name(self) -> str:
        return self.__name



class Rectangle(Shape) :
    __height : float
    __width : float

    def __init__(self, height : float, width : float) :
        self.__height = height
        self.__width = width
    
    def calc_area(self):
        return self.__height * self.__width

    def __str__(self) -> str:
        return f"Rectangle(height={self.__height}, width={self.__width})"

    def get_info(self) -> str:
        print(f"Height : {self.__height}")
        print(f"Width : {self.__width}")



class circle(Shape) : 
    __radius : float

    def __init__(self, radius : float) :
        self.__radius = radius
    
    def calc_area(self):
        return 3.14 * self.__radius * self.__radius

    def __str__(self) -> str:
        return f"Circle(radius={self.__radius})"

a = Rectangle(5, 4) 
b = circle(3)


print("Area of rectangle : ", a.calc_area())
print("Area of circle : ", b.calc_area())




print(a)


print(a.get_name())






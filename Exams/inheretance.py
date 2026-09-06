class Bike : 
    __name : str 
    __size : int 
    __gear_count : int 
    __terrain : str
    def __init__(self, name : str, size : int, gear_count : int, terrain : str) :
        self.__name = name 
        self.__size = size 
        self.__gear_count = gear_count 
        self.__terrain = terrain

    def info (self) : 
        print(f"Name: {self.__name}, Size: {self.__size}, Gear Count: {self.__gear_count}, Terrain: {self.__terrain}") 

    def ride(self) : 
        print(f"{self.__name} is being ridden on {self.__terrain} terrain.")

def Mountainbike (Bike) :
    __full_suspension : bool


    def __init__(self, name : str, size : int, gear_count : int, terrain : str, full_suspension : bool) :
        super().__init__(name, size, gear_count, terrain)
        self.__full_suspension = full_suspension
    def clean(self) : 
        print(f"{self.__name} is being cleaned.")

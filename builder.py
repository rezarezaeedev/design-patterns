'''
read more in 'Dive into design pattern' book or https://refactoring.guru/design-patterns/builder
Builder is a creational design pattern, let's your construct complex object step by step and more simple. The pattern allows you to produce different types and representations of an object using the same construction code.
    3 section: 1.Concrete Builders, 2.Director
-- E.g: About house
'''

class HouseBuilder:
    __walls = []
    __roofs = []
    __yards = []
    __doors = []
    __garage = []
    __windows = []

    def build_wall(self):
        self.__walls.append(Wall())

    def build_roof(self):
        self.__roof.append(Roof())

    def build_yard(self):
        self.__yard.append(Yard())

    def build_door(self):
        self.__doors.append(Door())

    def build_window(self):
        self.__windows.append(Window())

    def build_garage(self):
        self.__garage.append(Garage())


class Wall:
    def __str__(self) -> str:
        return 'A wall'

class Roof:
    def __str__(self) -> str:
        return 'A roof'

class Yard:
    def __str__(self) -> str:
        return 'A yard'

class Door:
    def __str__(self) -> str:
        return 'A door'

class Window:
    def __str__(self) -> str:
        return 'A window'
    
class Garage:
    def __str__(self) -> str:
        return 'A garage'

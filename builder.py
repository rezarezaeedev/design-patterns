'''
read more in 'Dive into design pattern' book or https://refactoring.guru/design-patterns/builder
Builder is a creational design pattern, let's your construct complex object step by step and more simple. The pattern allows you to produce different types and representations of an object using the same construction code.
    3 section: 1.Concrete Builders, 2.Director
-- E.g: About house
'''
from abc import ABC, abstractmethod


class Car:
    def __init__(self) -> None:
        self.__engine = None
        self.__wheels = []
        self.__body = None
        self.name:str
        self.model:str
    
    def attach_wheel(self, wheel):
        self.__wheels.append(wheel)

    def set_engine(self, engine):
        self.__engine = engine

    def set_body(self, body):
        self.__body = body

    def specification(self):
        print(f'* There is a {self.name} {self.model} Car with {self.__engine} engine, {self.__body} body and {len(self.__wheels)} wheels,')

class Wheel:
    def __init__(self, size) -> None:
        self.size = size
    def __str__(self) -> str:
        return f'{self.size}inch'

class Body:
    def __init__(self, color) -> None:
        self.color = color
    def __str__(self) -> str:
        return f'{self.color}'

class Engine:
    def __init__(self, name, power) -> None:
        self.name = name
        self.power = power
    def __str__(self) -> str:
        return f'{self.name} {self.power}cc'


class AbstractBaseBuilder(ABC):
    def get_engine(self): pass
    def get_wheel(self): pass
    def get_body(self): pass

class CarBuilder(AbstractBaseBuilder):

    def get_engine(self, name, power):
        return Engine(name, power)
        
    def get_wheel(self, size): 
        return Wheel(size)

    def get_body(self, color): 
        return Body(color)


class Director:
    __builder = None

    def set_builder(self, builder):
        self.__builder = builder
        
    def get_benz_suv(self):
        car = Car()
        builder = self.__builder

        engine = builder.get_engine('m15', '1500')
        car.set_engine(engine)

        body = builder.get_body('Gray')
        car.set_body(body)

        car.name = 'Benz'
        car.model = 'Suv'

        suv_car_wheels_count = 4
        suv_wheel_size = 24
        for i in range(suv_car_wheels_count):
            wheel = builder.get_wheel(suv_wheel_size)
            car.attach_wheel(wheel)
        return car

    def get_volvo_trailer(self):
        car = Car()
        builder = self.__builder

        engine = builder.get_engine('fh', '4000')
        car.set_engine(engine)

        body = builder.get_body('Red')
        car.set_body(body)

        car.name = 'Volvo'
        car.model = 'Trailer'

        trailer_car_wheels_count = 12
        trailer_wheel_size = 30
        for i in range(trailer_car_wheels_count):
            wheel = builder.get_wheel(trailer_wheel_size)
            car.attach_wheel(wheel)
        return car
    
    def get_bmw_sedan(self):
        car = Car()
        builder = self.__builder

        engine = builder.get_engine('m7', '4500')
        car.set_engine(engine)

        body = builder.get_body('Black')
        car.set_body(body)

        car.name = 'Bmw'
        car.model = 'Sedan'

        sedan_car_wheels_count = 4
        sedan_wheel_size = 22
        for i in range(sedan_car_wheels_count):
            wheel = builder.get_wheel(sedan_wheel_size)
            car.attach_wheel(wheel)
        return car


def main():
    director = Director()
    director.set_builder(CarBuilder())

    benz_suv = director.get_benz_suv()
    benz_suv.specification()

    volvo_trailer = director.get_volvo_trailer()
    volvo_trailer.specification()

    bmw_sedan = director.get_bmw_sedan()
    bmw_sedan.specification()

main()


        
    

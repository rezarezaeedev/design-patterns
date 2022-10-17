from copy import deepcopy
from pyexpat import model
from unicodedata import name

class Prototype:
    def __init__(self) -> None:
        self._objects={}
    
    def register(self, name:str, obj):
        self._objects.update({name:obj})
    def unregister(self, name):
        del self._objects[name]
    
    def clone(self, name, modified:dict={}):
        obj = self._objects.get(name)
        if obj:
            obj = deepcopy(obj)
            obj.__dict__.update(modified)
            return obj
        raise NameError(f'Not found any objects by {name} name.')


class Car:
    def __init__(self, name, company) -> None:
        self.name = name
        self.company = company
    def __str__(self) -> str:
        return f'Car object: {self.company}/{self.name}'


class Customer:
    def __init__(self, name, age, position, salary) -> None:
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
    def __str__(self) -> str:
        return f'Customer object: Mr. {self.name} is {self.age} with {self.salary}$ salary.'

# Test
prototype = Prototype()
car1 = Car('S500', 'Benz')
prototype.register('rezaee-car' ,car1)
customer1 = Customer('Reza Rezaee', 23, 'Programer','6000')
prototype.register('mr-rezaee' ,customer1)

customer2=prototype.clone('mr-rezaee')
print(customer2)
print('customer2 is customer1:', customer2 is customer1)

customer3=prototype.clone('mr-rezaee', {'name':'ms-alavi', })
print(customer1)
print(customer2)
print(customer3)

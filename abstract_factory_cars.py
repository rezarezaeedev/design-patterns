'''
    Car -> Benz, Bmw -> Suv, Sedan
        Suv:
            benz: GLA, GLS
            bmw:  x4,  x6
        Sedan: 
            benz: c200, s200
            bmw:  series5, series7
'''
from abc import ABC, abstractmethod
from optparse import Option


#-------------Entities
class BaseAbstractCar(ABC):
    def __init__(self, owner, plate_num, option='low/middle/full') -> None:
        self.owner = owner
        self.plate_num = plate_num
        self.option=option

# Companies
class BenzCompany(ABC):
    company = 'Benz/Germany'

class BmwCompany(ABC):
    company = 'Bmw/Germany'       

# Class Types
class BaseAbstractSedan(ABC):
    class_type = 'Sedan'

class BaseAbstractSuv(ABC):
    class_type = 'Suv'

# Car models
class C200(BaseAbstractCar, BenzCompany, BaseAbstractSedan):
    '''Do anything unique for this class type'''
    def __str__(self) -> str:
        return f'Benz Sedan Car: C class {self.option} option for mr {self.owner}'

class GLS(BaseAbstractCar, BenzCompany, BaseAbstractSuv):           
    def __str__(self) -> str:
        return f'Benz Suv Car: G class {self.option} option for mr {self.owner}'

class S500(BaseAbstractCar, BenzCompany, BaseAbstractSedan):    
    def __str__(self) -> str:
        return f'Benz Sedan Car: S class {self.option} option for mr {self.owner}'

class Series5(BaseAbstractCar, BmwCompany, BaseAbstractSedan):
    def __str__(self) -> str:
        return f'bmw Sedan Car: 5 series {self.option} option for mr {self.owner}'   


class Series7(BaseAbstractCar, BmwCompany, BaseAbstractSedan):
    def __str__(self) -> str:
        return f'bmw Sedan Car: 7 series {self.option} option for mr {self.owner}'   


class X6(BaseAbstractCar, BmwCompany, BaseAbstractSuv):
    def __str__(self) -> str:
        return f'bmw Suv Car: X 6 series {self.option} option for mr {self.owner}'   

#
#-------------Factories
class BaseAsbtractFactory(ABC):
    sedans:dict
    suvs:dict
    @abstractmethod
    def create_sedan(model):
        pass

    @abstractmethod
    def create_suv(model):
        pass

class BenzFactory(BaseAsbtractFactory):
    '''Do anything unique for company factory'''
    sedans={'c200':C200, 's500':S500} # please config product classes.
    suvs={'gls':GLS}
    def create_sedan(self, model, **data):
        sedan_class=self.sedans.get(model)
        if sedan_class:
            sedan = sedan_class(**data)
            return sedan
        raise NameError('Not found model name')
    
    def create_suv(self, model, **data):
        suv_class=self.suvs.get(model)
        if suv_class:
            suv = suv_class(**data)
            return suv
        raise NameError('Not found model name')

class BmwFactory(BaseAsbtractFactory):
    sedans={'series5':Series5, 'series7':Series7,}
    suvs={'x6':X6,}
    def create_sedan(self, model, **data):
        sedan_class=self.sedans.get(model)
        if sedan_class:
            sedan = sedan_class(**data)
            return sedan
        raise NameError('Not found model name')
    
    def create_suv(self, model, **data):
        suv_class=self.suvs.get(model)
        if suv_class:
            suv = suv_class(**data)
            return suv
        raise NameError('Not found model name')
#
#-------------Client
def order_sedan_car(factory:object, model, data:dict):
    my_car = factory.create_sedan(model, **data)
    return my_car

def order_suv_car(factory:object, model,data:dict):
    my_car = factory.create_suv(model, **data)
    return my_car

#
#-------------Test
data={'owner':'Rezaee', 'plate_num':'12b442', 'option':'full'}
car = order_sedan_car(BenzFactory(), 's500', data)
print(car)

data={'owner':'Rezaee', 'plate_num':'12b442', 'option':'full'}
car = order_suv_car(BmwFactory(), 'x6', data)
print(car)




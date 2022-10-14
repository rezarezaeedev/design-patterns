'''
    Car -> Benz, Bmw -> Suv, Sedan
        Suv:
            benz: GLA, GLS
            bmw:  x4,  x6
        Sedan: 
            benz: c200, s200
            bmw:  series5, series7
'''
from abc import ABC, abstractclassmethod


class Car:
    pass
#---------

class Benz(Car):
    pass

class Bmw(Car):
    pass
#---------

class Suv():
    pass

class Sedan():
    pass
#---------

class Gls:
    pass

class c200:
    pass

class X4:
    pass

class series5:
    pass
#---------

def order():
    pass


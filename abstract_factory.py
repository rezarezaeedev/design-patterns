'''
read more in digitalocean: https://www.digitalocean.com/community/tutorials/abstract-factory-design-pattern-in-java
Abstract Factory design pattern, 
    3 section: 1.Entities, 2.Factories, 3.Client

-- E.g: about a computer factory,
-- description: now we can develope program easy, just write products class and factory's class.
'''
from abc import ABC, abstractclassmethod, abstractmethod


# Entities or Products
class BaseComputer(ABC): 
    '''Base abstract product class'''
    ram:int
    hdd:int
    cpu:str
    @abstractclassmethod
    def __init__(self, ram, hdd, cpu) -> None:
        pass

    def __str__(self) -> str:
        return f'{self.__class__.__name__} Object: {self.name} ,ram:{self.ram}GB, hdd:{self.hdd}GB, cpu:{self.cpu}'

class PC(BaseComputer):
    '''An entity or a product'''
    def __init__(self, pcname, ram, hdd, cpu) -> None:
        self.pcname = pcname
        self.ram = ram
        self.hdd = hdd
        self.cpu = cpu
        self.name=pcname

class Server(BaseComputer):
    def __init__(self, servername, ram, hdd, cpu) -> None:
        self.servername = servername
        self.ram = ram
        self.hdd = hdd
        self.cpu = cpu
        self.name=servername

#----------------------------------------------------
# Factories
class BaseComputerFactory(ABC): 
    @abstractmethod
    def create_computer(**kw_data):
        pass

class PcFactory(BaseComputerFactory):
    @staticmethod # staticmethod for we dont want to need instance of this.
    def create_computer(**kw_data):
        return PC(**kw_data)


class ServerFactory(BaseComputerFactory):
    @staticmethod # staticmethod for we dont want to need instance of this.
    def create_computer(**kw_data):
        return Server(**kw_data)

#----------------------------------------------------
# Client or consumer
def order_computer(factory, data:dict): 
    computer = factory.create_computer(**data)
    return computer

#----------------------------------------------------
# Testing
def main_test():
    def test_pc():
        print('Pc test:')
        data={'pcname':'Reza PC', 'ram':'16', 'hdd':'1024', 'cpu':'Core i9 9400f'}
        pc = order_computer(PcFactory(), data)
        assert isinstance(pc, PC)
        print(pc,'\n')
    def test_server():
        print('Server test:')
        data={'servername':'CenntOs Server', 'ram':'256', 'hdd':'10000 ', 'cpu':'xeon'}
        server = order_computer(ServerFactory(), data)
        assert isinstance(server, Server)
        print(server,'\n')

    test_pc()
    test_server()
main_test()



'''
Adapter is a structural design pattern,
    included 3 section: 1.Adaptee, 2.Adapter, 3.Client
'''

class MotorCycle:
    def __init__(self) -> None:
        self.name = 'Motor Cycle'
    def TwoWheeler(self):
        return 'Two Wheeler'

class Truck:
    def __init__(self) -> None:
        self.name = 'Truck'
    def EightWheeler(self):
        return 'Eight Wheeler'

class Car:
    def __init__(self) -> None:
        self.name = 'Car'
    def FourWheeler(self):
        return 'Four Wheeler'

class Adapter:
    def __init__(self, vehicle, wheeler):
        self.vehicle  = vehicle
        self.vehicle.wheeler = wheeler
    # def __init__(self, vehicle, **adapted_methods):
    #     self.vehicle  = vehicle
    #     self.vehicle.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the vehicle object"""
        return getattr(self.vehicle, attr)
 
    def original_dict(self):
        """Print original vehicle dict"""
        return self.vehicle.__dict__
    
def main():
    adapteds_list = []

    motor = MotorCycle()
    adapted = Adapter(motor, wheeler=motor.TwoWheeler)
    adapteds_list.append(adapted)
    
    truck = Truck() 
    adapted = Adapter(truck, wheeler=truck.EightWheeler)
    adapteds_list.append(adapted)
    
    car = Car()
    adapted = Adapter(car, wheeler=car.FourWheeler)
    adapteds_list.append(adapted)

    for adapted in adapteds_list:
        print(f'A {adapted.name} is a {adapted.wheeler()} vehicle.')
        print('vehicle __dict__:',adapted.original_dict())
        print('\n')


main()



'''
Facade is a structural design pattern,
    That provides a simpified interface to a library, a framework, or any complex set of classes.
'''


class CPU:
    def execute(self):
        print('** CPU is executing processes...')

class Memory:
    def cache(self):
        print('** Memory was cache anything...')

class GPU:
    def draw(self):
        print('** GPU is drawing an image...')

class Battery:
    def on_battery(self):
        print('** The Computer uses battery power...')
    def on_plugin(self):
        print('** The Computer uses AC power...')

class HDD:
    def load(self):
        print('** Hard disk was load anything...')


class Computer: # A Facade
    def __init__(self) -> None:
        self.cpu = CPU()
        self.gpu = GPU()
        self.battery = Battery()
        self.hdd = HDD()
        self.memory = Memory()

    def turn_on(self):
        self.cpu.execute()
        self.gpu.draw()
        self.battery.on_battery()
        self.hdd.load()
        self.memory.cache()
        print('The Computer is ready to usage.')
    
    def turn_off(self):
        del self.cpu
        del self.gpu
        del self.battery
        del self.hdd
        del self.memory
        print('The Computer turned off.')


def main():
    computer = Computer()
    computer.turn_on()
    print()
    computer.turn_off()
main()

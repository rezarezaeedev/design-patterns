'''
Decorator is a structural design pattern, 
    That let's you to change and add behaviours before and after instanication a class or calling fucntion.
    tip 1: Decorator pattern is not equal to python decorator feature but these used for a same goal.
    tip 2: first function of decorator structure excutre in runtime even you dont call it.
'''

class Decorator:
    _component = None
    def __init__(self, component):
        self._component = component

    def hello_to_other(self, *args, **kwargs):
        print('before calling...')
        result = self._component.hello_to_other(*args, **kwargs)
        print('after calling...')
        return result


class Human:
    def __init__(self, name) -> None:
        self.name = name
    
    def hello_to_other(self, other_name):
        return f'Hello {other_name}, I am {self.name},'


def main():
    deco1=Decorator(Human('Reza'))
    print(deco1.hello_to_other('Sara'))
    print()

    deco2=Decorator(Human('Ahamd'))
    print(deco2.hello_to_other('Meysam'))
    print()
    
    print(deco2.hello_to_other('Fateme'))

main()

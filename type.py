class KlassBase:
    '''An abstract class'''
    def __init__(self, name, age) -> None:
        self.name = name
        self.age=age

    def hello(self):
        print(f'Hello {self.name}...')


def age_func_outside_class(self):
    print(f'{self.name} is {self.age} old.')


klass = type('klass', (KlassBase,), {'default':'The default value', 'person_age':age_func_outside_class})

k=klass('Reza',23)
k.hello()
k.person_age()
print(k.default)
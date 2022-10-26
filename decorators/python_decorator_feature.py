'''
Python decorator is a python feature that allow you to modify func or class behaviours.
'''

# Python Decorator
# don't forget @wrapper for saving meta-data.
def notify_decorator(deco_arg):
    print(f'decorator given argument: "{deco_arg}"')
    def outer_wrapper(func_or_class):
        def inner_wrapper(*args, **kwargs): # args, kwrags for calling class or function
            print('before func/class calling')
            result = func_or_class(*args, **kwargs)
            print('after func/class calling')
            return result
        return inner_wrapper
    return outer_wrapper


@notify_decorator('test arg')
def any_func(name):
    return f'Hello {name}'


@notify_decorator('test arg for class')
class any_class:
    def __init__(self, name) -> None:
        self.name = name 
    def __str__(self) -> str:
        return f'Hello {self.name}, An object.'


@notify_decorator('test arg for test func 2')
def for_test_tip_2_func(name):
    return f'Hello {name}'


# Test
def main():
    print('function called...')
    print(any_func('Reza'))
    print()
    print('class called...')
    print(any_class('Ali'))


main()

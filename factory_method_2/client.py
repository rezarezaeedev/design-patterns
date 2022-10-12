'''
Factory Method: Is acreational design pattern,
    3 Component -> 1.Creator, 2.Product, 3.Client

-- E.g: The example is about file editing module in scalable program by class programming.
'''
from creators import get_creator_class


class File:
    def __init__(self, name, format):
        self.name=name
        self.format=format
    

def editor(file):
    creator_class = get_creator_class(file.format)
    creator = creator_class(file)
    file_object = creator.make()
    print(file_object.edit())


my_file = File('test', 'py')
my_file_2 = File('index', 'html')
# my_file_3 = File('scripts', 'xml') # error

editor(my_file)
editor(my_file_2)
# editor(my_file_3)


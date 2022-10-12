from abc import ABC, abstractmethod
from products import PythonFile, HtmlFile


class Creator(ABC):
    @abstractmethod
    def make(self):
        pass

    def __init__(self, file) -> None:
        self.file = file


class PythonCreator(Creator):
    def make(self):
        # Do anything to making a python file object and return.
        return PythonFile()


class HtmlCreator(Creator):
    def make(self):
        # Do anything to making a python file object and return.
        return HtmlFile()



class IdentifierError(ValueError):
    pass


def identifier_error(format='your'):
    raise IdentifierError(f'Not found any creator by {format} identifier.')


_creators_dict = {'py':PythonCreator, 'html':HtmlCreator}

def get_creator_class(format):
    result = _creators_dict.get(format,)
    if result:
        return result
    raise  identifier_error()

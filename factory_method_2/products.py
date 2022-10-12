from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def edit(self):
        pass


class PythonFile(Product):
    def edit(self):
        return 'The python file was editted.'


class HtmlFile(Product):
    def edit(self):
        return 'The html file was editted.'

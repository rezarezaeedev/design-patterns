'''
Factory Method: A creational design pattern,
    3 Components -> 1.Creator, 2.Product, 3.Client

-- The example code is about file editing module.
'''

class File:
    def __init__(self, name, format):
        self.name=name
        self.format=format
    

class Editor:
    def edit(self, file): # Client func
        editor = self._get_editor(file.format)
        print('Result =>',editor(file))

    def _get_editor(self, format): # Creator func
        result:None
        if format == 'xml': # *.format is identifier
            result = self.xml_editor
        elif format == 'pdf':
            result = self.html_editor
        elif format == 'html':
            result = self.html_editor
        else:
            raise ValueError('The file format not supported.')
        return result
        
    def xml_editor(self, file): # Product
        return f'The {file.name}.{file.format} file was edited.'

    def html_editor(self, file):
        return f'The {file.name}.{file.format} file was edited.'

    def pdf_editor(self, file):
        return f'The {file.name}.{file.format} file was edited.'


# User where using client 
file = File('index', 'html')
editor = Editor()
editor.edit(file)

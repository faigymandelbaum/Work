
class Rectangle:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        self.__length = int(value) 

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = int(value)            
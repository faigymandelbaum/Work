
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = int(value) 

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = int(value)            
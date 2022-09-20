#!/usr/bin/python3
"""

Rectangle Module


Defines a Rectangle with width and height

"""

class Rectangle:
    """Rectangle with width and height attributes"""
    def __init__(self, width=0, height=0):
        self.width = width
        self. height = height

    @property
    def width(self):
        return self._width

    @width.setter
    property setter def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
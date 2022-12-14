#!/usr/bin/python3
""" This Module defines a Rectangle with width and height.
"""


 class Rectangle:
    """rectangle with width and height attributes"""

    def __init__(self, width=0, height=0):
        """initializes a new rectangle object with width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self._width

    @width.setter 
    def width(self, value):
        """Sets the width of the rectangle"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

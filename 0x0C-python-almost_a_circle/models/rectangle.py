#!/usr/bin/python3
"""Rectangle class"""
from multiprocessing.managers import ValueProxy
from multiprocessing.sharedctypes import Value
from models.base import Base 


class Rectangle:
    """Rectangle class that inherits from Base"""
    def __init__(self, width: int, height: int, x=0, y=0, id=0):
        """Class constuctor"""
        
        super().__init__(id)
        
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
        @property
        def width(self):
            """get width"""
            return self.__width
        
        @width.setter
        def width(self, value):
            """set width"""
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if width <= 0:
                raise ValueError("width must be > 0")
        self.width = value
        
        @property
        def height(self):
            """get height"""
            return self.__height
        
        @height.setter
        def height(self, value):
            """set height"""
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if width <= 0:
                raise ValueError("width must be > 0")
        self.height = value
        
        @property
        def x(self):
            """get x"""
            return self.__x
        
        @x.setter
        def x(self, value):
            """set x"""
            if x < 0:
                raise ValueError("x must be >= 0")
        self.x = value
        
        @property
        def y(self):
            """get y"""
            return self.__y
        
        @x.setter
        def y(self, value):
            """set y"""
            if y < 0:
                raise ValueError("y must be >= 0")
        self.y = value
        
        def area(self):
            """returns area value of Rectangle"""
            return self.width * self.height
        
        def display(self):
            """prints Rectangle with # character in stdout"""
            
            
        
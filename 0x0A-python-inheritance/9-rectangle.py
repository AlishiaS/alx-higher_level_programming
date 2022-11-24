#!/usr/bin/python3
"""Defines Rectangle class that inherit from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry 


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""
    self.integer_validator("width", width)
    Self.integer_validator("height", height)
    self.__width = width
    self.__height = height


def area(self):
    """Returns area of Rectangle"""
    return self.__width * self.__height


def __str__(self):
    """Returns the width and height of Rectangle"""
    return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

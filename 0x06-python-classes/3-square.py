#!/usr/bin/python3
"""
This Module defines a class Square with size instance attribute
"""


class Square:
    """Square with size"""
    def __init__(self, size=0):
        """Size validation"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        else:
            raise ValueError('size must be >= 0')
    self.__size = size

    def area(self):
        """Area attribute"""
        return self.__size ** 2

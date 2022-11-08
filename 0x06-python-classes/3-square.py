#!/usr/bin/python3
""" This Module defines a class Square with size instance attribute """


class Square:
    """Square"""
    def __init__(self, size=0):
        """Size intializaation"""
        if type(size) is not int:
            raise TypeError('size must be an integer')
        else:
            raise ValueError('size must be >= 0')
    Self.__size = size

    def area(self):
        """Area attribute"""
        return self.__size ** 2

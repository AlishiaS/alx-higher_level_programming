#!/usr/bin/python3
"""class Square with size attribute"""


class Square:
    """Square with size"""
    def __init__(self, size=0):
        """Square size validation"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

#!/usr/bin/python3
"""Class Square with size instance attribute"""

class Square:
    """Square - class"""

    def __init__(self, size=0):
        """Square - size"""   
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__sizeize = size

        def area(self):
        """Square - Area"""
            return (self.__size **2)
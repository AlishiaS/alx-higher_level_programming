#!/usr/bin/python3
"""Square class #2"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size


    def __str__(self):
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)

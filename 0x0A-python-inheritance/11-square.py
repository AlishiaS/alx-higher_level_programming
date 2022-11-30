#!/usr/bin/python3
"""Square class #2"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""
    def __init__(self, size):
        """Instantiation"""
        try:
            super().__init__(size, size)
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be greater than 0")
        self.__size = size

    def __str__(self):
        return '[Square] {size}/{size}'.format(size=self.__size)

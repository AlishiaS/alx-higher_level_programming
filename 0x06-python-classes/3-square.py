#!/usr/bin/python3
""" This Module defines a class Square with size instance attribute """


class Square:
    """Square with:
        Attribute: size
    """
    def __init__(self, size=0):
        """ Square initialization
        Args:
            size (int): size of square
        Returns: 
                Nothing
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        else:
            raise ValueError('size must be >= 0')
    self.__size = size

    def area(self):
        """Calculates area of the square
        Returns:
                Area of the square
        """
        return (self.__size) ** 2

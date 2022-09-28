#!/usr/bin/python3
"""Square #1"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle"""
    def __init__(self, size):
        super().__init__(size, size)

#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base 


class Rectangle:
    """Rectangle class that inherits from Base"""
    def __init__(self, width: int, height: int, x=0, y=0, id=0):
        """ """
        
        super().__init__(id)
        
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
#!/usr/bin/python3
"""square class"""
from itertools import zip_longest
from models.rectangle import Rectangle

class Square:
    """Class Square that inherits from REctangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)
        self.__size = size
        
    @property
    def size(self) -> int:
        """get size"""
        return self.__size
    
    @size.setter
    def size(self, value: int):
        """set size"""
        self.__size = value
        self.width = self.height = value 
        
    def __str__(self) -> str:
        """string representation of class Square"""
        id = self.id
        x = self.x
        y = self.y
        size = self.__size
        return "[Square] ({}) {}/{} - {}/{}".format(id, x, y, size)
    
    def update(self, *args, **kwargs):
        """update Square"""
        att = ['id', 'size', 'x', 'y']
        if args:
            for a, n, in zip(att, args):
                setattr(self, a, n)
        elif kwargs:
            for k, value in kwargs.items():
                if k in att:
                    setattr(self, k, value)
    
    def to_dictionary(self) -> dict:
        """Dictionary representation of Square"""
        id = self.id
        x = self.x
        y = self.y
        size = self.__size
        return {'id': id, 'x': x, 'y': y, 'size': size}
    
    
    
    
    
        
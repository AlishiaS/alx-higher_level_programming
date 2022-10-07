#!/usr/bin/python3
"""Rectangle class"""
from models.base import Base 


class Rectangle:
    """Rectangle class that inherits from Base"""
    def __init__(self, width: int, height: int, x=0, y=0, id=0):
        """Class constuctor"""
        
        super().__init__(id)
        
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        
        @property
        def width(self):
            """get width"""
            return self.__width
        
        @width.setter
        def width(self, value):
            """set width"""
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if width <= 0:
                raise ValueError("width must be > 0")
        self.width = value
        
        @property
        def height(self):
            """get height"""
            return self.__height
        
        @height.setter
        def height(self, value):
            """set height"""
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if width <= 0:
                raise ValueError("width must be > 0")
        self.height = value
        
        @property
        def x(self):
            """get x"""
            return self.__x
        
        @x.setter
        def x(self, value):
            """set x"""
            if x < 0:
                raise ValueError("x must be >= 0")
        self.x = value
        
        @property
        def y(self):
            """get y"""
            return self.__y
        
        @x.setter
        def y(self, value):
            """set y"""
            if y < 0:
                raise ValueError("y must be >= 0")
        self.y = value
        
        def area(self):
            """returns area value of Rectangle"""
            return self.width * self.height
        
        def display(self):
            """prints Rectangle with # character in stdout"""
            print('\n'*self.y, end='')
            for n in range(self.height):
                print(' '*self.x + '#'*self.width)
        
        def __str__(self) -> str:
            """string representation of Rectangle"""
            
            return "[Rectangle] ({}) {}/{} - {}/{}" \
                .format(self.id, self.height, self.width, self.x, self.y)
                
                
        def update(self, *args, **kwargs):
            """update Rectangle"""
            
            expect = (self.id, self.width, self.height, self.x, self.y)
            if args != ():
                self.id, self.width, self.height, self.x, self.y = \
                   args + expect[len(args):len(expect)]
            elif kwargs:
                for (name, value) in kwargs.items():
                    setarr(self, name, value)
                    
        def to_dictionary(self):
            """dictionary representation of Rectangle"""
            
            return {
                'id':self.id,
                'height':self.height,
                'width':self.width,
                'x':self.x,
                'y':self.y
            }

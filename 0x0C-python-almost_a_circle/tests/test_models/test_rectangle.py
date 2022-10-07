#!/usr/bin/python3
"""rectangle unittests"""

import unittest
from models.rectangle import Rectangle

class TeastRectaangle(unittest.TestCase):
    """Test for Rectangle"""
    
    if __name__ == '__main__':
        unittest.main
        
    def test_initialization(self):
        rec1 = Rectangle(1, 3)
        rec2 = Rectangle(2, 4)
        self.assertEqual(rec1.id, Rectangle._Base_nb_objects)
        self.assertEqual(rec2.id, Rectangle._Base_nb_objects)
        
#!/usr/bin/python3
"""rectangle unittests"""

import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    """Test for Square"""
    
    if __name__ == '__main__':
        unittest.main

    
    def test_initialization_without_arguments(self):
        self.assertRaises(TypeError, Square)
        
    def test_initialization_success(self):
        sqre1 = Square(1, 3)
        sqre2 = Square(2, 4)
        self.assertEqual(sqre1.id, 2)
        self.assertEqual(sqre2.id, 3)
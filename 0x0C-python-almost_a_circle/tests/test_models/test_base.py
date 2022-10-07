#!/usr/bin/python3
"""base unittests"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """unit test for Base"""
    
    if __name__ == '__main__':
        unittest.main
    
    def test_to_json_string_valid(self):
        pass
    
    def test_saving_id(self):
        base = Base(50)
        self.assertEqual(base.id, 50)
        
    def test_initialization(self):
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        
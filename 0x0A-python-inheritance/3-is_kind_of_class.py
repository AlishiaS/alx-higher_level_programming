#!/usr/bin/python3
"""
Defines a function to check if a object is an instance of a class or
an instance of an inherited class
"""


def is_kind_of_class(obj, a_class):
    """Returns true or false"""
    if isinstance(obj, a_class):
        return True
    return False

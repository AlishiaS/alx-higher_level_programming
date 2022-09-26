#!/usr/bin/python3
"""
Defines a function to check if the object is an instance of a class
that inherited from the specified class
"""


def inherits_from(obj, a_class):
    """Returns true or false"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

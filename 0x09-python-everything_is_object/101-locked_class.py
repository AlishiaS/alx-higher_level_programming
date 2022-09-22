#!/usr/bin/python3
"""Module defines a LockedClass"""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance attibutes
    except if the new instance attribute is called first_name
    """

    __name__ = ["first_name"]

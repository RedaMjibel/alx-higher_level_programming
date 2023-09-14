#!/usr/bin/python3
"""Documentation"""


def add_attribute(obj, attr, val):
    """checks if it is possible to add attr and then does it"""
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, val)
    else:
        raise TypeError("can't add new attribut")

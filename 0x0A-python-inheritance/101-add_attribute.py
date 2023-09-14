#!/usr/bin/python3
"""Documentation"""


def add_attribute(obj, attr, val):
    """checks if it is possible to add attr and then does it"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, val)

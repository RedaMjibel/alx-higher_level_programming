#!/usr/bin/python3
"""Documentation"""


def inherits_from(obj, a_class):
    """checks if an object is an instance of a class that inherited"""
    return type(obj) != a_class and isinstance(obj, a_class)

#!/usr/bin/python3
"""Documentation"""


def is_kind_of_class(obj, a_class):
    """Determines if an object is an instance of a class or a subclass"""
    if isinstance(obj, a_class):
        return True
    else:
        return False

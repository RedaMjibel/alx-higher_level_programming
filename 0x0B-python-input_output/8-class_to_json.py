#!/usr/bin/python3
"""Documentation"""


def class_to_json(obj):
    """returns the dictionary description for
        JSON serialization of an object"""
    return obj.__dict__

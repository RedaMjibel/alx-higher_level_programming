#!/usr/bin/python3
"""Documentation"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__
        for attr in attrs:
            if type(attr) is not str:
                return self.__dict__
        thisdict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                thisdict[key] = value
        return thisdict

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)

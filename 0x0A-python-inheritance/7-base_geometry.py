#!/usr/bin/python3
"""Documentation"""


class BaseGeometry:
    """an empty class"""
    def area(self):
        """public instance method"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """Public instance method that validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

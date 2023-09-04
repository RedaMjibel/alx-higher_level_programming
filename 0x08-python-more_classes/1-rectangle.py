#!/usr/bin/python3
"""Documentation"""


class Rectangle:
    """This is a rectangle"""
    def __init__(self, width=0, height=0):
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """property to retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter to set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """property to retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        self.__height = value

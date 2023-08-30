#!/usr/bin/python3
"""Documentation"""


class Square:
    """This is a class"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """method"""
        return self.__size ** 2

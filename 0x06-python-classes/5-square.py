#!/usr/bin/python3
"""Documentation"""


class Square:
    """This is a class"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """property to retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter to set value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """method"""
        return self.__size ** 2

    def my_print(self):
        """print method"""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="\n" if j is self.size - 1 and i != j else "")
        print()

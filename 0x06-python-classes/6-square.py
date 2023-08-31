#!/usr/bin/python3
"""Documentation"""


class Square:
    """This is a class"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """property to retrieve size"""
        return self.__position

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and value[0] > 0 and
            isinctace(value[1], int) and value[1] > 0:
                self.__position = value
        raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """method"""
        return self.__size ** 2

    def my_print(self):
        """print method"""
        if self.__size == 0:
            print("")
            return
        for i in range(0, self.__position[1]):
            print("")
        for j in range(self.__size):
            for k in range(0, self.__position[0]):
                print(" ", end="")
            for p in range(0, self.__size):
                print("#", end="")
            print("")

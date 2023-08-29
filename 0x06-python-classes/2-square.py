#!/usr/bin/python3
"""Documentation"""


class Square:
    """square class"""
    def __init__(self, size=0):
        """instanitation"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

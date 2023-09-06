#!/usr/bin/python3
"""Module for the add_integer method"""

def add_integer(a, b=98):
    """Adds 2 integers.

    Args:
        a: the first integers
        b: the second integer with a default value 98

    Raises:
        TypeError: if a, b are not int, float

    Returns:
        The sumf of two integers
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")

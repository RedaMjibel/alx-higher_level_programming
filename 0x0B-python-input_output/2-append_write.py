#!/usr/bin/python3
"""Documentation"""


def append_write(filename="", text=""):
    """appends a string and the end of a text file"""
    with open(filename, "a", encoding="utf-8") as myfile:
        return myfile.write(text)

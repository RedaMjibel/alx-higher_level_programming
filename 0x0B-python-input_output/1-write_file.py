#!/usr/bin/python3
"""Documentation"""


def write_file(filename="", text=""):
    """writes a string to a text file"""
    with open(filename, "w", encoding="utf-8") as myfile:
        return myfile.write(text)

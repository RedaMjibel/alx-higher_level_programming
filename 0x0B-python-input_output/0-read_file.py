#!/usr/bin/python3
"""Documentation"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout"""
    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read(), end="")

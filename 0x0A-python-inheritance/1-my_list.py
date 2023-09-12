#!/usr/bin/python3
"""Documentation"""


class MyList(list):
    """Mylist inherits list"""
    def print_sorted(self):
        """Method that prints the list in sorted order"""
        print(sorted(self))

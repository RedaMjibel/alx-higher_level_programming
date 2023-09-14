#!/usr/bin/python3
"""Documentation"""


class MyInt(int):
    """class MyInt that inherits from int"""
    def __eq__(self, obj):
        """inverts the behavior of the eq operator"""
        return super().__ne__(obj)

    def __ne__(self, obj):
        """inverts the behavior of the ne operator"""
        return super().__eq__(obj)

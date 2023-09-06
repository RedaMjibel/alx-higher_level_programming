#!/usr/bin/python3
class LockedClass:
    __slots__ = ("first_name",)

    def __init__(self, first_name=None):
        if first_name is not None:
            self.first_name = first_name

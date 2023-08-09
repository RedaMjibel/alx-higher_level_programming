#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if 97 <= ord(char) <= 122:
            uppercase = chr(ord(char) - 32)
            print("{}".format(uppercase), end="")
        else:
            print(f"{char}")

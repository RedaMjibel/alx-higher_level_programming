#!/usr/bin/python3
def uppercase(str):
    string = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            uppercase = chr(ord(char) - 32)
            string = string + uppercase
        else:
            string = string + char
    print("{}".format(string))

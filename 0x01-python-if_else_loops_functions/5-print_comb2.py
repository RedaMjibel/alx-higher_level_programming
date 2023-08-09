#!/usr/bin/python3
for number in range(99):
    if 0 <= number <= 9:
        print("0{}".format(number), end=", ")
    else:
        print("{}".format(number), end=", ")


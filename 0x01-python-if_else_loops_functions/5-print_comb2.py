#!/usr/bin/python3
for number in range(100):
    if 0 <= number <= 9:
        print("0{}".format(number), end=", ")
    else:
        print("{}".format(number), end=", " if number < 99 else "\n")


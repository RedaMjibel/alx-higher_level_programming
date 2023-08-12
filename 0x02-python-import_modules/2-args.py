#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_arguments = len(sys.argv) - 1
    if num_arguments == 1:
        print("{} argument:".format(num_arguments))
    elif num_arguments == 0:
        print("{} arguments.".format(num_arguments))
    else:
        print("{} arguments:".format(num_arguments))
    for index in range(num_arguments):
        print("{}: {}".format(index + 1, sys.argv[index + 1]))

#!/usr/bin/python3
import sys

if __name__ == "__main__":
    num_arguments = len(sys.argv) - 1
    results = 0
    for index in range(num_arguments):
        results = results + int(sys.argv[index + 1])
    print("{}".format(results))

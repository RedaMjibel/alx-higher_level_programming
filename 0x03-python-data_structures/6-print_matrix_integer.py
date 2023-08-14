#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for inside_list in matrix:
        for number in inside_list:
            print("{}".format(number), end=" ")
        print()

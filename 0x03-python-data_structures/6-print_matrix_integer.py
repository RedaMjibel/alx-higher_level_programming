#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for inside_list in matrix:
        for number in inside_list:
            print("{:d}".format(number),
                  end=" "if number != inside_list[-1] else "")
        print()

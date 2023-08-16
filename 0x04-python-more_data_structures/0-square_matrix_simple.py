#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        sublist = []
        for numbers in i:
            sublist.append(numbers ** 2)
        new_matrix.append(sublist)
    return (new_matrix)

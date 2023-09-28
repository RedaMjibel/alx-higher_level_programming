#!/usr/bin/python3
"""Documentation"""


def matrix_divided(matrix, div):
    """Divides all elements in a matrix"""
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    result = [[0 for _ in row] for _ in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[i][j] = round(matrix[i][j] / div, 2)
    return result


if __name__ == "__main__":

    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqrd_matrix = matrix.copy()

    for n in range(len(matrix)):
        sqrd_matrix[n] = list(map(lambda x: x**2, matrix[n]))

    return (sqrd_matrix)

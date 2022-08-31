#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqrd_matrix = matrix.copy()

    for i in range(len(matrix)):
        sqrd_matrix = list(map(lamda x: x**2, matrix[i]))

    return (sqrd_matrix)

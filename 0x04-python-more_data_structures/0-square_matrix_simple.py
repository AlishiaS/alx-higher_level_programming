#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqrd_matrix = []

    for n in range(len(matrix)):
        sqrd_matrix.append(n**2 for n in matrix)

    return sqrd_matrix

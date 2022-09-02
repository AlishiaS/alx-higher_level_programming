#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqrd_matrix = []

    for list in matrix:
        sqrd_matrix.append([n**2] for n in list)

    return sqrd_matrix

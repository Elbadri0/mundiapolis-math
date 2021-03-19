#!/usr/bin/env python3
"""
the traspose of a matrix
"""


def matrix_transpose(matrix):
    """
    entre the matrix
    and Returns the traspose of the matrix
    """
    tras = []
    for row in range(len(matrix[0])):
        tras.append([matrix[col][row] for col in range(len(matrix))])
    return tras

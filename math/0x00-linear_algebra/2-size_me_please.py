#!/usr/bin/env python3
"""
calculate the shape
"""


def matrix_shape(matrix):
    """
    entre the matrix
    and Returns the shape in a list
    """
    if type(matrix[0]) is not list:
        return [len(matrix)]
    else:
        return [len(matrix)] + matrix_shape(matrix[0])

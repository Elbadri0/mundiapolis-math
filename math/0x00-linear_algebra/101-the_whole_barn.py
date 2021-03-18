#!/usr/bin/env python3
"""
add two matrices
"""


def matrix_shape(matrix):
    """
    enter a matrix
    and Returns the shape as a list
    """
    if type(matrix[0]) is not list:
        return [len(matrix)]
    else:
        return [len(matrix)] + matrix_shape(matrix[0])


def add_recursive(mat1, mat2):
    """
    enter a matrix
    Returns the resulting matrix
    """
    if type(mat1[0]) is not list:
        return [mat1[i] + mat2[i] for i in range(len(mat1))]
    else:
        result = []
        for i in range(len(mat1)):
            inner = add_recursive(mat1[i], mat2[i])
            result.append(inner)
        return result


def add_matrices(mat1, mat2):
    """
    enter a matrix
    Returns the resulting matrix
    """
    if matrix_shape(mat1) != matrix_shape(mat2):
        return None
    else:
        return add_recursive(mat1, mat2)

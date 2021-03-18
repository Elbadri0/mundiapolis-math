#!/usr/bin/env python3
"""Contains the add_matrices function"""


def shape(matrix):
    """ calculates the matrix shape """
    shape = [len(matrix)]
    while type(matrix[0]) == list:
        shape.append(len(matrix[0]))
        matrix = matrix[0]
    return shape


def rec_cat_matrices(mat1, mat2, axis, depth):
    """recursivly concat two matrices"""
    matrix = []

    if depth == axis:
        matrix = mat1 + mat2
        return matrix

    for i in range(len(mat1)):
        matrix.append(rec_cat_matrices(mat1[i], mat2[i], axis, depth + 1))
    return matrix


def cat_matrices(mat1, mat2, axis=0):
    """that concatenates two matrices along a specific axis"""

    shape1 = shape(mat1)
    shape2 = shape(mat2)

    shape1.pop(axis)
    shape2.pop(axis)
    if shape1 != shape2 or axis >= len(shape1) + 1:
        return None
    depth = 0
    return rec_cat_matrices(mat1, mat2, axis, depth)

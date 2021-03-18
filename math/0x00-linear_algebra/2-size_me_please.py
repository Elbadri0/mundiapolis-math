#!/usr/bin/env python3
    """
    how calculate the shape
    """


def matrix_shape(matrix):
    """
 enter matrix
 and Returns the shapein a list
    """
    if type(matrix[0]) is not list:
        return [len(matrix)]
    else:
        return [len(matrix)] + matrix_shape(matrix[0])

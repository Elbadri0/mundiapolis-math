#!/usr/bin/env python3
"""
operations on matrices
"""


def np_elementwise(mat1, mat2):
    """
    enter a matrix
    and Returns the result
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)

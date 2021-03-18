#!/usr/bin/env python3
"""
multiplication of two matrices
"""


def mat_mul(mat1, mat2):
    """
    enter a matrix
    and Returns a new matrix multiplied
    """
    if len(mat1[0]) == len(mat2):
        new = []
        for row1 in range(len(mat1)):
            inner = []
            for col2 in range(len(mat2[0])):
                number = 0
                for col1 in range(len(mat1[0])):
                    number += (mat1[row1][col1] * mat2[col1][col2])
                inner.append(number)
            new.append(inner)
        return new
    else:
        return None

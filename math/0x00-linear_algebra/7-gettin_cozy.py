#!/usr/bin/env python3
"""
concatenating of two matrices with specific axis
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    enter a matrix
    and Returns a list of concatenated matrices
    """
    if (len(mat1[0]) == len(mat2[0])) and (axis == 0):
        concat = [ele.copy() for ele in mat1]
        concat += [ele.copy() for ele in mat2]
        return concat
    elif (len(mat1) == len(mat2)) and (axis == 1):
        concat = [mat1[j] + mat2[j] for j in range(len(mat1))]
        return concat
    else:
        return None

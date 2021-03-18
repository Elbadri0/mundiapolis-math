#!/usr/bin/env python3
"""
multiplies two matrices with numpy with slices
"""


def np_slice(matrix, axes={}):
    """
    enter a matrix
    and Returns the result
    """
    sliced = []
    max_key = max(axes)
    for i in range(max_key + 1):
        if i in axes.keys():
            sliced.append(slice(*axes.get(i)))
        else:
            sliced.append(slice(None, None, None))
    return matrix[tuple(sliced)]

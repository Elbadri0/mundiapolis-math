#!/usr/bin/env python3
"""
concatenating two matrices with numpy
"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    enter a matrix
    and Returns the result
    """
    return np.concatenate((mat1, mat2), axis=axis)

#!/usr/bin/env python3
"""
concatenating
"""


def cat_arrays(arr1, arr2):
    """
    entre a matrix 
    and Returns a list of arrays concatenated
    """
    concated = arr1.copy()
    for i in arr2:
        concated.append(i)
    return concated

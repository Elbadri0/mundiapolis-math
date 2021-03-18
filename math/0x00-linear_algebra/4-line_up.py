#!/usr/bin/env python3
"""
calculate the sum of two arrays
"""


def add_arrays(arr1, arr2):
    """
    entre the matrix
    and Returns the sum 
    """
    if len(arr1) != len(arr2):
        return None
    return [(arr1[i] + arr2[i]) for i in range(len(arr1))]

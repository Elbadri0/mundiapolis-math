#!/usr/bin/env python3


def matrix_shape(matrix):
    if type(matrix[0]) is not list:
        return [len(matrix)]
    else:
        return [len(matrix)] + matrix_shape(matrix[0])


def add_recursive(mat1, mat2):
    if type(mat1[0]) is not list:
        return [mat1[i] + mat2[i] for i in range(len(mat1))]
    else:
        result = []
        for i in range(len(mat1)):
            inner = add_recursive(mat1[i], mat2[i])
            result.append(inner)
        return result


def add_matrices(mat1, mat2):
    if matrix_shape(mat1) != matrix_shape(mat2):
        return None
    else:
        return add_recursive(mat1, mat2)

#!/usr/bin/env python3
def add_matrices2D(mat1, mat2):
    if len(mat1) != len(mat2):
        return None
    elif len(mat1[0]) != len(mat2[0]):
        return None
    else:
        new_mat = [[mat1[i][j] + mat2[i][j]
                    for j in range(len(mat1[0]))] for i in range(len(mat1))]
        for count in new_mat:
            return new_mat

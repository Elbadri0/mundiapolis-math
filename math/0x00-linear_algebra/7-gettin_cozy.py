#!/usr/bin/env python3

def cat_matrices2D(mat1, mat2, axis=0):
    if (len(mat1[0]) == len(mat2[0])) and axis == 0:
        new_mat1 = [x[:] for x in mat1]
        new_mat2 = [x[:] for x in mat2]
        new_mat = new_mat1 + new_mat2
        return new_mat
    elif (len(mat1) == len(mat2)) and axis == 1:
        new_mat = [mat1[x] + mat2[x] for x in range(len(mat1))]
        return new_mat
    else:
        return None

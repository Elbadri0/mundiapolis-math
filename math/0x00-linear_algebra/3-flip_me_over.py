#!/usr/bin/env python3
def matrix_transpose(matrix):
    new_matrix = []
    for i in range(len(matrix[0])):
        N_row = []
        for j in range(len(matrix)):
            N_row.append(matrix[j][i])
        new_matrix.append(N_row)
    return new_matrix
  

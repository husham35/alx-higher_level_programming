#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if matrix:
        temp_matrix = [[item ** 2 for item in row] for row in matrix]
        return temp_matrix
    else:
        return matrix

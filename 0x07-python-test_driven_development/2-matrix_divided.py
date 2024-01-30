#!/usr/bin/python3
"""
Module for the definition of the `matrix_divided` function
"""


def matrix_divided(matrix, div):
    """
    Function to divide a matrix's elements by a given number
    Args:
        matrix: (matrix) the matrix to divide
        div: (int) the divisor
    Raises:
        TypeError: if matrix is not a list of lists of integers/floats
        TypeError: if each row of the matrix does not have the same size
        TypeError: if any element of the matrix is not an int/float
        TypeError: if div is not an integer/float
        ZeroDivisionError: if div is 0
    Returns:
        list of lists: new matrix
    """

    l_err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    r_err_msg = "Each row of the matrix must have the same size"
    div_err_msg = "div must be a number"
    div_zero_msg = "division by zero"

    if not (isinstance(matrix, list) or not all(isinstance(rows, list) for rows in matrix)):
        raise TypeError(l_err_msg)

    row_size = len(matrix[0])
    for rows in matrix:
        if any(type(el) not in (int, float) for el in rows):
            raise TypeError(l_err_msg)
        if len(rows) != row_size:
            raise TypeError(r_err_msg)

        if type(div) not in (int, float):
            raise TypeError(div_err_msg)
        if div == 0:
            raise ZeroDivisionError(div_zero_msg)

        return [[round(el / int(div), 2) for el in rows] for rows in matrix]

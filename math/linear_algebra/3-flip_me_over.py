#!/usr/bin/env python3
"""Module that transposes a 2D matrix."""


def matrix_transpose(matrix):
    """Return the transpose of a 2D matrix as a new matrix."""
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[i][j] for i in range(rows)] for j in range(cols)]

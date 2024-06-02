#!/usr/bin/python3


def rotate_2d_matrix(matrix):
    """rotates 2d matrix 90 clockwise"""
    n = len(matrix)

    for i in range(n):
        for j in range(i):
            # Swap elements at position(i, j) with elements at position(j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse rows
    for i in range(n):
        matrix[i] = matrix[i][::-1]

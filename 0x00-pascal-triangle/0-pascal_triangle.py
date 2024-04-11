#!/usr/bin/python3
"""
Pascal's result
"""


def pascal_triangle(n):
    """
    Funtion for a pascal results implementation
    return: the list of lists of int representing the pascal's
            result of n
    """
    result = []
    if type(n) is not int or n <= 0:
        return result
    for i in range(n):
        line = []
        for j in range(i + 1):
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(result[i - 1][j - 1] + result[i - 1][j])
        result.append(line)
    return result

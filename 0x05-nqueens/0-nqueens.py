#!/usr/bin/env python3
"""N queens problem"""

import sys


def init():
    """Validation point

    Returns:
        N(int)
    """
    # checks for the correct num of command-line args
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit:
        N = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    return N


def formatted_solution(positions):
    """Formats the solution for printing"""
    formatted_solution = [[row, col] for row, col in enumerate(positions)]
    return formatted_solution


def nqueens():
    N = init()


if __name__ == "__main__":
    nqueens()

#!/usr/bin/python3
"""N queens problem"""

import sys


def init():
    """Validation point

    Returns:
        N(int): Number of queens
    """
    # checks for the correct num of command-line args
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    # Validates if N is an integer
    if sys.argv[1].isdigit():
        N = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    return N


def is_valid(positions, row, col):
    """Checks to see if the queen can be placed at row or col"""
    for i in range(row):
        if (
            positions[i] == col
            or positions[i] - i == col - row
            or positions[i] + i == col + row
        ):
            return False
    return True


def solve_nqueens(size, row, positions, solutions):
    """Recursively puts the queens on the board and sotres the solution"""
    if row == size:
        solutions.append(positions[:])
    else:
        for col in range(size):
            if is_valid(positions, row, col):
                positions[row] = col
                solve_nqueens(size, row + 1, positions, solutions)


def solution_format(positions):
    """Formats the solution for printing"""
    formatted_solution = [[row, col] for row, col in enumerate(positions)]
    return formatted_solution


def nqueens():
    """entry point"""
    N = init()

    # Finding all solutions
    solutions = []
    positions = [-1] * N
    solve_nqueens(N, 0, positions, solutions)

    # print out a formatted output of all solutions
    for solution in solutions:
        print(solution_format(solution))


if __name__ == "__main__":
    nqueens()

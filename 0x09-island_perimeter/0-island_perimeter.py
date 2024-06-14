#!/usr/bin/python3
""" Island perimeter computing module
"""


def island_perimeter(grid):
    """Calculates the perimeter of an island"""
    perimeter = 0

    if not isinstance(grid, list):
        return 0

    # get the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])

    """Loop through each cell in the grid"""
    for row in range(rows):
        for col in range(cols):
            """check all four sides"""
            if grid[row][col] == 1:
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                if row == rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                if col == cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1

    return perimeter

#!/usr/bin/env python3
"""The minimum operations coding challenge
"""


def minOperations(n):
    """Computes the fewest number of operations needed to result
    in exactly n H characters.
    args: Number of characters to be displayed
    return: number of minimum operations
    """
    if not isinstance(n, int):
        return 0
    now = 1
    start = 0
    counter = 0
    while now < n:
        remainder = n - now
        if remainder % now == 0:
            start = now
            now += start
            counter += 2
        else:
            now += start
            counter += 1
    return counter

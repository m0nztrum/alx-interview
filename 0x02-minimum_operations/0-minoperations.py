#!/usr/bin/env python3
"""The minimum operations coding challenge
"""


def minOperations(n):
    """Computes the fewest number of operations needed to result
    in exactly n H characters.
    """
    if not isinstance(n, int):
        return 0
    opr_count = 0
    clipboard = 0
    done = 1
    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            opr_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            opr_count += 2
        elif clipboard > 0:
            done += clipboard
            opr_count += 1
    return opr_count

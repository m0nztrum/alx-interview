#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    A function that determine the fewest number
    of coins needed to meet a given total

    Args:
        - coins (list): A list of coins
        - total (int): Amount to be met

    Returns:
        - int: fewest number of coins needed to make total.
        - If total <= 0 return 0.
        - If total can't be met by any num of coins you have return -1.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        while coin <= total:
            total -= coin
            count += 1

    if total != 0:
        return -1

    return count

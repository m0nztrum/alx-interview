#!/usr/bin/python3
"""Prime game
"""


def isWinner(x, nums):
    """Determines the winner of a prime game with 'x' rounds"""
    if x <= 0 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    max_num = max(nums)

    # sieve
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(max_num**0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, max_num + 1, i):
                is_prime[multiple] = False

    prime_counts = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_counts[i] = prime_counts[i - 1] + (1 if is_prime[i] else 0)

    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    if ben_wins > maria_wins:
        return "Ben"
    return None

#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """method that calculates the
    fewest number of operations needed
    to result in exactly n H characters
    in the file.
    """

    if n <= 1:
        return 0

    # Initialize an array to store minimum operations for each count of characters
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = i
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)  # Take the minimum of current value and possible combination of factors

    return dp[n]

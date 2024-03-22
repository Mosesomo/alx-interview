#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n: int) -> int:
    """method that calculates the
    fewest number of operations needed
    to result in exactly n H characters
    in the file.
    """

    if n <= 1:
        return 0
    
    min_operations = float('inf')
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            min_operations = min(min_operations, i + n // i)

    return min_operations


#!/usr/bin/env python3
"""Minimum Operations"""


def minOperations(n):
    """method that calculates the
    fewest number of operations needed
    to result in exactly n H characters
    in the file.
    """

    if n <= 1:
        return 0
    min_operations = 0
    current_len = 1
    while current_len < n:
        if n % current_len == 0:
            min_operations += 1  # copy all operation
            current_len *= 2  # paste operation
        else:
            current_len += current_len  # paste operation
        min_operations += 1
    return min_operations

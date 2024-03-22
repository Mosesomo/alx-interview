#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """method that calculates the
    fewest number of operations needed
    to result in exactly n H characters
    in the file.
    """

    current_len = 1
    clipboard = 0
    num_operations = 0

    while current_len < n:
        if clipboard == 0:
            # copyall
            clipboard = current_len
            # increment operations counter
            num_operations += 1

        # if haven't pasted anything yet
        if current_len == 1:
            # paste
            current_len += clipboard
            # increment operations counter
            num_operations += 1
            # continue to next loop
            continue

        remaining = n - current_len
        if remaining < clipboard:
            return 0

        if remaining % current_len != 0:
            current_len += clipboard
            num_operations += 1
        else:
            clipboard = current_len
            current_len += clipboard
            num_operations += 2
    if current_len == n:
        return num_operations
    else:
        return 0

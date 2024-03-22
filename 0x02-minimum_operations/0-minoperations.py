#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """method that calculates the
    fewest number of operations needed
    to result in exactly n H characters
    in the file.
    """

    pasted_chars = 1
    clipboard = 0
    counter = 0

    while pasted_chars < n:
        if clipboard == 0:
            # copyall
            clipboard = pasted_chars
            # increment operations counter
            counter += 1

        # if haven't pasted anything yet
        if pasted_chars == 1:
            # paste
            pasted_chars += clipboard
            # increment operations counter
            counter += 1
            # continue to next loop
            continue

        remaining = n - pasted_chars
        if remaining < clipboard:
            return 0

        if remaining % pasted_chars != 0:
            pasted_chars += clipboard
            counter += 1
        else:
            clipboard = pasted_chars
            pasted_chars += clipboard
            counter += 2
    if pasted_chars == n:
        return counter
    else:
        return 0

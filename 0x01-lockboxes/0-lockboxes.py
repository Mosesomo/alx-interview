#!/usr/bin/python3
"""Implementating lockboxes"""


def canUnlockAll(boxes):
    """Function implementation to determine if all boxes
        in  list can be unlocked
    """

    for key in range(1, len(boxes)):
        flag = False
        for box in range(len(boxes)):
            if key in boxes[box] and box != key:
                flag = True
                break
        if not flag:
            return False
    return True

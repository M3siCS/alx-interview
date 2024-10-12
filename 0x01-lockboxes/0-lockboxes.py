#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    :param boxes: List of lists containing keys for boxes
    :return: True if all boxes can be unlocked, False otherwise
    """
    n = len(boxes)  # Total number of boxes
    unlocked = [False] * n  # Track which boxes have been unlocked
    unlocked[0] = True  # Box 0 is unlocked by default
    stack = [0]  # Start with box 0
    
    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if 0 <= key < n and not unlocked[key]:  # Only consider valid keys
                unlocked[key] = True
                stack.append(key)  # Add newly unlocked box to the stack

    return all(unlocked)  # Return True if all boxes are unlocked


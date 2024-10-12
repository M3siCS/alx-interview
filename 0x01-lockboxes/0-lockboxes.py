#!/usr/bin/python3
def canUnlockAll(boxes):
    """Determines if all boxes can be opened"""
    n = len(boxes)
    unlocked = [False] * n  # Track which boxes have been unlocked
    unlocked[0] = True  # Box 0 is unlocked by default
    stack = [0]  # Start with box 0

    while stack:
        current_box = stack.pop()
        # Explore the keys in the current box
        for key in boxes[current_box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)  # Add the box to explore next

    # Return True if all boxes are unlocked
    return all(unlocked)

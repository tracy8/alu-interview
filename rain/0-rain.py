#!/usr/bin/python3
"""
Rainwater Trapping Module

This module contains a function to calculate the amount of rainwater that can
trapped between walls after it rains. The walls are represented by a list of
non-negative integers where each integer represents the height of a wall with
a unit width of 1.

Function:
    - rain(walls): Returns the total amount of rainwater retained given a list
      of wall heights.
"""


def rain(walls):
    """
    Calculate the total amount of rainwater that can be trapped btn the walls.

    Parameters:
    - walls (List[int]): A list of non-negative integers rprsntng the heights
      of the walls.

    Returns:
    - int: The total amount of rainwater retained.

    Example:
    >>> walls = [0, 1, 0, 2, 0, 3, 0, 4]
    >>> print(rain(walls))
    6
    >>> walls = [2, 0, 0, 4, 0, 0, 1, 0]
    >>> print(rain(walls))
    6
    """
    if not walls:
        return 0

    n = len(walls)
    left_max = [0] * n
    right_max = [0] * n

    # Fill left_max array
    left_max[0] = walls[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], walls[i])

    # Fill right_max array
    right_max[n - 1] = walls[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    # Calculate water retention
    water_retained = 0
    for i in range(n):
        water_retained += min(left_max[i], right_max[i]) - walls[i]

    return water_retained

# Example usage
if __name__ == "__main__":
    walls = [0, 1, 0, 2, 0, 3, 0, 4]
    print(rain(walls))  # Output: 6
    walls = [2, 0, 0, 4, 0, 0, 1, 0]
    print(rain(walls))

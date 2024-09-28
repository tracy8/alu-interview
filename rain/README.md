# Rainwater Trapping

## Problem Description

This project addresses the problem of calculating how much rainwater can be trapped between walls after rainfall. The walls are represented as a list of non-negative integers, where each integer corresponds to the height of the wall.

The challenge is to determine how many square units of water will be retained between the walls after rain, assuming that water is trapped between two higher walls.

## Solution

The solution involves:

1. Calculating the maximum height of the walls on the left and right for each position.
2. Determining the minimum of these two maximum heights.
3. Calculating the water retained by subtracting the height of the current wall from the minimum height.

The total water retained is the sum of the water trapped at each position.

## Example

For the walls `[0, 1, 0, 2, 0, 3, 0, 4]`, the total water retained is `6` units.

For the walls `[2, 0, 0, 4, 0, 0, 1, 0]`, the total water retained is also `6` units.

## Usage

To calculate the rainwater retained:

```python
from rain import rain

walls = [0, 1, 0, 2, 0, 3, 0, 4]
print(rain(walls))  # Output: 6

"""
'''
Description: the solution to Problem 64 - dynamic programming with space optimisation (using the original list)
Version: 1.0.0.20220214
Author: Arvin Zhao
Date: 2022-02-14 16:56:10
Last Editors: Arvin Zhao
LastEditTime: 2022-02-14 17:39:24
'''
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """Time complexity: O(n_columns * n_rows), space complexity: O(1)."""

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][
                        j - 1
                    ]  # One can only move right to make the point be on the 1st row.
                elif j == 0:
                    grid[i][j] += grid[i - 1][
                        j
                    ]  # One can only move down to make the point be on the 1st column.
                else:
                    grid[i][j] += min(grid[i][j - 1], grid[i - 1][j])

        return grid[-1][-1]

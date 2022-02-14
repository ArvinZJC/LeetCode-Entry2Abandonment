"""
Description: the solution to Problem 64 - dynamic programming with space optimisation (storing the last row results only)
Version: 1.0.0.
Author: Arvin Zhao
Date: 2022-02-14 17:18:49
Last Editors: Arvin Zhao
LastEditTime: 2022-02-14 17:38:22
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """Time complexity: O(n_columns * n_rows), space complexity: O(n_columns)."""

        n_columns = len(grid[0])
        dp = [0] * n_columns  # Dynamic programming.

        for i in range(len(grid)):
            for j in range(n_columns):
                if i == j == 0:
                    dp[j] = grid[i][j]
                elif i == 0:
                    dp[j] = (
                        grid[i][j] + dp[j - 1]
                    )  # One can only move right to make the point be on the 1st row.
                elif j == 0:
                    dp[j] = (
                        grid[i][j] + dp[j]
                    )  # One can only move down to make the point be on the 1st column.
                else:
                    dp[j] = grid[i][j] + min(dp[j - 1], dp[j])

        return dp[-1]

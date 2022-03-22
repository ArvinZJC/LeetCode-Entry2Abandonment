"""
'''
Description: Problem 64 (Minimum Path Sum) - Solution 1
Version: 1.0.1.20220322
Author: Arvin Zhao
Date: 2022-02-14 17:18:49
Last Editors: Arvin Zhao
LastEditTime: 2022-03-22 19:38:44
'''
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """Dynamic programming: time complexity: O(n_columns * n_rows), space complexity: O(n_columns * n_rows)."""
        n_columns = len(grid[0])
        n_rows = len(grid)
        dp = [[0] * n_columns for _ in range(n_rows)]  # Dynamic programming.

        for i in range(n_rows):
            for j in range(n_columns):
                dp[i][j] = grid[i][j]

                if i == j == 0:
                    continue
                elif i == 0:
                    dp[i][j] += dp[i][
                        j - 1
                    ]  # One can only move right to make the point be on the 1st row.
                elif j == 0:
                    dp[i][j] += dp[i - 1][
                        j
                    ]  # One can only move down to make the point be on the 1st column.
                else:
                    dp[i][j] += min(dp[i][j - 1], dp[i - 1][j])

        return dp[-1][-1]

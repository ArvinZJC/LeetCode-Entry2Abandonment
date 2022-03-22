"""
'''
Description: Problem 1 (Two Sum) - Solution 1
Version: 1.0.2.20220322
Author: Arvin Zhao
Date: 2022-02-10 21:25:31
Last Editors: Arvin Zhao
LastEditTime: 2022-03-22 19:34:16
'''
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Brute force: time complexity: O(n_nums ^ 2), space complexity: O(1)."""
        n_nums = len(nums)

        for i in range(n_nums):
            for j in range(i + 1, n_nums):
                if nums[i] + nums[j] == target:
                    return [i, j]

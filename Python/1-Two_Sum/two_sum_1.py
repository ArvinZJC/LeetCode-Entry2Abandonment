"""
'''
Description: the solution to Problem 1 - brute force
Version: 1.0.0.20220210
Author: Arvin Zhao
Date: 2022-02-10 21:25:31
Last Editors: Arvin Zhao
LastEditTime: 2022-02-10 21:39:06
'''
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_nums = len(nums)

        for i in range(n_nums):
            for j in range(i + 1, n_nums):
                if nums[i] + nums[j] == target:
                    return [i, j]

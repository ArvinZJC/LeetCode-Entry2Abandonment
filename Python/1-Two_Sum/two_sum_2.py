"""
Description: the solution to Problem 1 - hash table
Version: 1.0.0.20220210
Author: Arvin Zhao
Date: 2022-02-10 21:25:45
Last Editors: Arvin Zhao
LastEditTime: 2022-02-10 21:25:45
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}

        for i, num in enumerate(nums):
            if target - num in hash_table:
                return [hash_table[target - num], i]

            hash_table[num] = i  # Avoid num itself.

        return []

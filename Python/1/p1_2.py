"""
'''
Description: Problem 1 (Two Sum) - Solution 2
Version: 1.0.2.20220322
Author: Arvin Zhao
Date: 2022-02-10 21:25:45
Last Editors: Arvin Zhao
LastEditTime: 2022-03-22 19:34:31
'''
"""


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Hash table: time complexity: O(n_nums), space complexity: O(n_nums)."""
        hash_table = {}

        for i, num in enumerate(nums):
            if target - num in hash_table:
                return [hash_table[target - num], i]

            hash_table[num] = i  # Avoid num itself.

        return []

"""
'''
Description: Problem 912 (Sort an Array) - Solution 1
Version: 1.0.0.20220319
Author: Arvin Zhao
Date: 2022-03-19 12:58:01
Last Editors: Arvin Zhao
LastEditTime: 2022-03-19 14:16:33
'''
"""

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """Built-in stable sort function."""

        return sorted(nums)

"""
'''
Description: Problem 912 (Sort an Array) - Solution 3
Version: 1.0.0.20220319
Author: Arvin Zhao
Date: 2022-03-19 13:47:36
Last Editors: Arvin Zhao
LastEditTime: 2022-03-19 14:26:25
'''
"""

from heapq import heapify, heappop
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """Heap sort (unstable) using built-in functions."""

        heapify(nums)
        return [heappop(nums) for _ in range(len(nums))]

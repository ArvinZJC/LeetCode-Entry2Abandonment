"""
'''
Description: Problem 912 (Sort an Array) - Solution 2
Version: 1.0.0.20220322
Author: Arvin Zhao
Date: 2022-03-19 13:00:42
Last Editors: Arvin Zhao
LastEditTime: 2022-03-22 19:38:16
'''
"""

from random import randint
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """Quick sort using random pivots to partition: time complexity: O(n_nums * log(n_nums)), space complexity: O(n_recursion) (log(n_nums) <= n_recursion <= n_nums)."""

        def quick_sort(nums: List[int], left: int, right: int) -> None:
            if left >= right:
                return

            pivot = randint(left, right)
            nums[pivot], nums[right] = nums[right], nums[pivot]
            mid = left - 1

            for i in range(left, right):
                if nums[i] < nums[right]:
                    mid += 1
                    nums[i], nums[mid] = nums[mid], nums[i]

            mid += 1
            nums[mid], nums[right] = nums[right], nums[mid]
            quick_sort(nums, left, mid - 1)
            quick_sort(nums, mid + 1, right)

        quick_sort(nums, 0, len(nums) - 1)
        return nums

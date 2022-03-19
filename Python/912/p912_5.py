"""
'''
Description: Problem 912 (Sort an Array) - Solution 5
Version: 1.0.0.20220319
Author: Arvin Zhao
Date: 2022-03-19 14:59:30
Last Editors: Arvin Zhao
LastEditTime: 2022-03-19 15:36:57
'''
"""

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """Merge sort (stable): time complexity: O(n_nums * log(n_nums)), space complexity: O(n_nums)."""

        def merge_sort(nums: List[int], left: int, right: int) -> None:
            if left == right:
                return

            mid = (left + right) // 2
            merge_sort(nums, left, mid)
            merge_sort(nums, mid + 1, right)

            temp = []
            i = left
            j = mid + 1

            while i <= mid or j <= right:
                # Set this condition rather than the "i <= mid and nums[i] <= nums[j]" version to avoid being out of range for "j" due to "j > right".
                if i > mid or (j <= right and nums[i] > nums[j]):
                    temp.append(nums[j])
                    j += 1
                else:
                    temp.append(nums[i])
                    i += 1

            nums[left : right + 1] = temp

        merge_sort(nums, 0, len(nums) - 1)
        return nums

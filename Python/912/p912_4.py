"""
'''
Description: Problem 912 (Sort an Array) - Solution 4
Version: 1.0.0.20220322
Author: Arvin Zhao
Date: 2022-03-19 14:26:38
Last Editors: Arvin Zhao
LastEditTime: 2022-03-22 19:38:03
'''
"""

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """Self-implemented heap sort (unstable): time complexity: O(n_nums * log(n_nums)), space complexity: O(1)."""

        def max_heapify(nums: List[int], root: int, length: int) -> None:
            parent = root  # Set the initial parent index to the root index.

            while parent * 2 + 1 < length:
                left = parent * 2 + 1
                right = left + 1

                if right >= length or nums[left] > nums[right]:
                    parent_next = left
                else:
                    parent_next = right

                if nums[parent] >= nums[parent_next]:
                    break

                nums[parent], nums[parent_next] = nums[parent_next], nums[parent]
                parent = parent_next

        n_nums = len(nums)

        # "n_nums // 2 - 1" is used to reduce unnecessary loops due to the condition for the while statement in the function max_heapify().
        for i in range(n_nums // 2 - 1, -1, -1):
            max_heapify(nums, i, n_nums)

        for i in range(n_nums - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            max_heapify(nums, 0, i)

        return nums

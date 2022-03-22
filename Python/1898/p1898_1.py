"""
'''
Description: Problem 1898 (Maximum Number of Removable Characters) - Solution 1
Version: 1.0.0.20220322
Author: Arvin Zhao
Date: 2022-03-10 15:27:07
Last Editors: Arvin Zhao
LastEditTime: 2022-03-22 19:35:42
'''
"""

from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        """Binary search: time complexity: O(n_s * log(n_s)), space complexity: O(n_s)."""
        left = 0
        n_p = len(p)
        n_s = len(s)
        right = len(removable) + 1

        while left < right:
            mid = left + (right - left) // 2
            s_state = [True] * n_s  # Indicate if the specific character is kept.

            # Change the state to indicate deleting the characters specified by the first "mid" values in "removable".
            for i in range(mid):
                s_state[removable[i]] = False

            j = 0
            is_mid_left = True  # A flag indicating if k is on the middle's left.

            # Check if p is still a subsequence of the new s.
            for i in range(n_s):
                if s_state[i] and p[j] == s[i]:
                    j += 1

                    if j == n_p:
                        left = mid + 1
                        is_mid_left = False
                        break

            if is_mid_left:
                right = mid

        return left - 1

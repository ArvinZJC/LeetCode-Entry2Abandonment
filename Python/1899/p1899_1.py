"""
'''
Description: Problem 1899 (Merge Triplets to Form Target Triplet) - Solution 1
Version: 1.0.0.20220322
Author: Arvin Zhao
Date: 2022-03-10 19:33:29
Last Editors: Arvin Zhao
LastEditTime: 2022-03-22 19:36:15
'''
"""

from typing import List


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """Greedy: time complexity: O(n_triplets), space complexity: O(1)."""
        a = b = c = 0

        for a_i, b_i, c_i in triplets:
            if a_i <= target[0] and b_i <= target[1] and c_i <= target[2]:
                a, b, c = max(a, a_i), max(b, b_i), max(c, c_i)

        return [a, b, c] == target

"""
'''
Description: Problem 1897 (Redistribute Characters to Make All Strings Equal) - Solution 3
Version: 1.0.0.20220322
Author: Arvin Zhao
Date: 2022-03-10 14:48:21
Last Editors: Arvin Zhao
LastEditTime: 2022-03-22 19:36:25
'''
"""

from collections import Counter
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        """Checking if the count of each lowercase letters appeared is divisible (consider only the lowercase appeared with Python's built-in methods): time complexity: O(N + L) (N = SUM(n_word), 1 ≤ L ≤ 26), space complexity: O(L)."""
        n_words = len(words)
        return all(count % n_words == 0 for count in Counter("".join(words)).values())

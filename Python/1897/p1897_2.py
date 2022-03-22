"""
'''
Description: Problem 1897 (Redistribute Characters to Make All Strings Equal) - Solution 2
Version: 1.0.0.20220322
Author: Arvin Zhao
Date: 2022-03-10 14:26:50
Last Editors: Arvin Zhao
LastEditTime: 2022-03-22 19:36:33
'''
"""

from collections import defaultdict
from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        """Checking if the count of each lowercase letters appeared is divisible (consider only the lowercase appeared): time complexity: O(N + L) (N = SUM(n_word), 1 ≤ L ≤ 26), space complexity: O(L)."""
        lowercase_counts = defaultdict(
            int
        )  # A dictionary storing each existing lowercase letters' frequency.
        n_words = len(words)

        for word in words:
            for letter in word:
                lowercase_counts[letter] += 1

        return all(
            lowercase_count % n_words == 0
            for lowercase_count in lowercase_counts.values()
        )

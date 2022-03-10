"""
'''
Description: Problem 1897 (Redistribute Characters to Make All Strings Equal) - Solution 1
Version: 1.0.0.20220310
Author: Arvin Zhao
Date: 2022-03-10 13:58:02
Last Editors: Arvin Zhao
LastEditTime: 2022-03-10 15:54:02
'''
"""

from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        """Checking if the count of each lowercase letters appeared is divisible: time complexity: O(N + 26) (N = SUM(n_word)), space complexity: O(26)."""

        lowercase_counts = [
            0
        ] * 26  # A list used as a dictionary to store each lowercase letters' frequency (even if the lowercase may not appear).
        n_words = len(words)

        for word in words:
            for letter in word:
                lowercase_counts[ord(letter) - ord("a")] += 1

        return all(
            lowercase_count % n_words == 0 for lowercase_count in lowercase_counts
        )

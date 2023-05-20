# Challenge 2 - Valid Anagram
# Author: Julia Sabelli
# LEETCODE VERSION


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if (1 > len(s)) or (len(t) > (5 * (10 ** 4))):
            return False

        s = sorted(s.lower())
        t = sorted(t.lower())

        if s == t:
            return True
        else:
            return False


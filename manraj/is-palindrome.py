import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^0-9a-zA-Z]+', '', s.lower())
        n = len(s) - 1

        if n < 1: return True
        
        for i in range(n):
            if i == n: return True
            if s[i] != s[n]: return False
            n -= 1

        return True

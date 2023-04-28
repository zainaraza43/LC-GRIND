# Given a string s, return true if it is a palindrome, or false otherwise.

import re

class Solution(object):
    def isPalindrome(self, s):
        s = re.sub(r'[^\w\s]', '', s)
        s = s.replace(" ", "")
        s = s.replace("_", "")
        s_lower = s.lower()
        reversed_s = s[::-1]
        reversed_s = reversed_s.replace(" ", "")
        reversed_lower = reversed_s.lower()

        if s_lower == reversed_lower:
            return True
        else:
            return False

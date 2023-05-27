# Challenge 4 - Valid Palindrome
# Author: Julia Sabelli
# LEETCODE VERSION


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())

        if s == ''.join(reversed(s)):
            return True
        else:
            return False


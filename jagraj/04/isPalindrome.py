class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().strip()
        r = ""
        for i in s:
            if i in "abcdefghijklmnopqrstuvwxyz0123456789":
                r += i
        return r == r[::-1]

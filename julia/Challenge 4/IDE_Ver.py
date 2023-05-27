# Challenge 4 - Valid Palindrome
# Author: Julia Sabelli
# IDE VERSION


import re


def isPalindrome(s: str) -> bool:
    s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())

    if s == ''.join(reversed(s)):
        return True
    else:
        return False


class Solution:

    if __name__ == '__main__':

        print("Testcase 1 = ", isPalindrome("A man, a plan, a canal: Panama"))
        print("\nTestcase 2 = ", isPalindrome("race a car"))
        print("\nTestcase 3 = ", isPalindrome(" "))


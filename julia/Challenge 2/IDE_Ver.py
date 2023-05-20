# Challenge 2 - Valid Anagram
# Author: Julia Sabelli
# IDE VERSION


def isAnagram(s: str, t: str) -> bool:

    if (1 > len(s)) or (len(t) > (5 * (10 ** 4))):
        return False

    s = sorted(s.lower())
    t = sorted(t.lower())

    if s == t:
        return True
    else:
        return False


class Solution:

    if __name__ == '__main__':

        print("Testcase 1 = ", isAnagram("anagram", "nagaram"))
        print("\nTestcase 2 = ", isAnagram("rat", "car"))


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}

        for i in s:
            counts[i] = counts.get(i, 0) + 1

        for i in t:
            if i not in counts:
                return False
            counts[i] -= 1
            if counts[i] == -1:
                return False

        for c in counts.values():
            if c != 0:
                return False

        return True

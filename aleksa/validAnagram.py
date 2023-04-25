class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #Time complexity: O(s+t)
        #Memory complexity: O(s+t)

        if len(s) != len(t): return False

        Sset = {}
        Tset = {}

        for i in range(len(s)):
            Sset[s[i]] = Sset.get(s[i], 0) + 1
            Tset[t[i]] = Tset.get(t[i], 0) + 1
        return Sset == Tset
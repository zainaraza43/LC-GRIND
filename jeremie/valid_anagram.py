class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss, tt = {}, {}
        for i in s:
            ss[i] = ss.get(i, 0)+1
        for i in t:
            tt[i] = tt.get(i, 0)+1
        return ss == tt
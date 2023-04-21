class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = {i: s.count(i) for i in set(s)} #hot one liners 
        t_dict = {i: t.count(i) for i in set(t)}
        if s_dict == t_dict:
            return True
        else:
            return False
        
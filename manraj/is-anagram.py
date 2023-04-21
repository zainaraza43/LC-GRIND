class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        s_dict = dict()
        t_dict = dict()

        for c in s:
            if (c in s_dict):
                s_dict[c] = s_dict[c] + 1
            else:
                s_dict[c] = 1
        
        for c in t:
            if (c in t_dict):
                t_dict[c] = t_dict[c] + 1
            else:
                t_dict[c] = 1
        
        if (s_dict == t_dict):
            return True
        else:
            return False

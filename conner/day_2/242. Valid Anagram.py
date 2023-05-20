class Solution:
    def isAnagram(self, s: str, t: str) -> bool:        
        lt = list(t)
        
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] in lt:
                    lt.remove(s[i])

        if len(lt) == 0:
            return True
                    
        return False

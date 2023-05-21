class Solution:
    # My Solution
    def isPalindrome(self, s: str) -> bool:
        j = len(s) - 1
        
        for i in range(len(s)):
            if (s[i] >= 'A' and s[i] <= 'Z') or (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= '0' and s[i] <= '9'):
                while not ((s[j] >= 'A' and s[j] <= 'Z') or (s[j] >= 'a' and s[j] <= 'z') or (s[j] >= '0' and s[j] <= '9')):
                    j -= 1

                if s[i].lower() != s[j].lower():
                    return False
                j -= 1
        
        return True
    
    # Thought it was smart and wanted to remember it
    def isPalindrome(self, s: str) -> bool:
        noSpace = ("".join(filter(str.isalnum, s))).lower()
        return noSpace == noSpace[::-1]
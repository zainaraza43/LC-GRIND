class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        newString = ""
        s = s.lower()

        for letter in range(len(s)):
            if (ord(s[letter]) <= 122 and ord(s[letter]) >= 97) or (ord(s[letter]) <= 57 and ord(s[letter]) >= 48):
                newString += s[letter]    
        return newString == newString[::-1]
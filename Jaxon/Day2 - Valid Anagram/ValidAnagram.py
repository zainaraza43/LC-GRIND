class Solution(object):
    def isAnagram(self, s, t):
        sLetters = []
        tLetters = []

        for letter in range(len(s)):
            sLetters.append(s[letter])

        for letter in range(len(t)):
            tLetters.append(t[letter])
        
        for letter in range(len(s)):
            if s[letter] in tLetters:
                tLetters.remove(s[letter])
                sLetters.remove(s[letter])
        
        if tLetters == [] and sLetters == []:
            return True
        else: return False


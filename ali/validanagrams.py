class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1 = {}
        string2 = {}

        for letter in s:
            string1[letter] = string1.get(letter, 0) + 1
        
        for letter in t:
            string2[letter] = string2.get(letter, 0) + 1
        
        print("first:", string1.values(), "second:", string2.values())
        return string1 == string2
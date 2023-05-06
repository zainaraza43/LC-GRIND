# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        dict_s = {}
        dict_t = {}
        for char in s:
            if char in dict_s:
                dict_s[char]+=1
            else:
                dict_s[char]=1

        for char in t:
            if char in dict_t:
                dict_t[char]+=1
            else:
                dict_t[char]=1
        
        if dict_s == dict_t:
            return True

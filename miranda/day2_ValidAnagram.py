class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


#driver code
s = "anagram"
t = "nagaram"

solution = Solution()
print(solution.isAnagram(s, t))
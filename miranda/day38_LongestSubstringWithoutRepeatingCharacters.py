class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seenChars = set()
        left = 0
        longestLength = 0

        for right in range(len(s)):
            while s[right] in seenChars:
                seenChars.remove(s[left])
                left += 1
            seenChars.add(s[right])
            longestLength = max(longestLength, right - left + 1)
        return longestLength

s = "abcabcbb"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))
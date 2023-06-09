class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = 0
        max_interval = 0
        window = set()
        for i, c in enumerate(s):
            if c in window:
                max_interval = max(max_interval, len(window))
                while s[a] != c:
                    window.remove(s[a])
                    a += 1
                window.remove(s[a])
                a += 1
            window.add(c)
        max_interval = max(max_interval, len(window))
        return max_interval

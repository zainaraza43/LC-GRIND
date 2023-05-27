from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        c = set()

        for i in nums:
            c.add(i)

        result = 0
        for i in c:
            if i - 1 not in c:
                current = 0
                while (i + current) in c:
                    current += 1
                result = max(result, current)
        return result




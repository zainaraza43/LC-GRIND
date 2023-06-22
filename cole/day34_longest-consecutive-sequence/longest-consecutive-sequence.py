from functools import cache

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        d = {num: num for num in nums}

        @cache
        def foo(num) -> int:
            if num + 1 in d:
                d[num] = foo(num + 1)
                return d[num]
            return num
        for num in nums:
            foo(num)
        return max([v - k for k, v in d.items()]) + 1

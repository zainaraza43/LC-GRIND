from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = num ^ res
        return res

nums = [4, 1, 2, 1, 2]
solution = Solution()
print(solution.singleNumber(nums))
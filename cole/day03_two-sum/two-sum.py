# beats 89.71%

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            if (target - num) in d:
                return (i, d[target - num])
            d[num] = i

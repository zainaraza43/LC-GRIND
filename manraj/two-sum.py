class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i,j in enumerate(nums):
            if target - j in values:
                return (values[target - j], i)
            values[j] = i

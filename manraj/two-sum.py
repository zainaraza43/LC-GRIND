class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = dict()
        for i,j in enumerate(nums):
            if target - j in values:
                return (values[target - j], i)
            else:
                values[j] = i

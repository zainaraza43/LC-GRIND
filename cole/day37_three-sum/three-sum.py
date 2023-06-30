from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            a = i + 1
            b = len(nums) - 1
            target = -nums[i]
            while a < b:
                if nums[a] + nums[b] == target and sorted([nums[i], nums[a], nums[b]]) not in res:
                    res.append(sorted([nums[i], nums[a], nums[b]]))
                if nums[a] + nums[b] < target:
                    a += 1
                else:
                    b -= 1
        return res
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = dict()
        for x, num in enumerate(nums):
            if (target-num) in hashMap:
                return [x, hashMap[target-num]]
            hashMap[num] = x
        
        return [-1, -1]
    
#driver code
nums = [10, 11, 12]
target = 23
solution = Solution()
print(solution.twoSum(nums, target))
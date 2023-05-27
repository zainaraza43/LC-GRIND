from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        retArr = [0 for i in range(len(nums))]
        size = len(nums) - 1

        prefix = 1
        for i, num in enumerate(nums):
            retArr[i] = prefix
            prefix *= num

        postfix = 1
        for i, num in enumerate(reversed(nums)):
            retArr[size - i] *= postfix
            postfix *= num 

        return retArr
    
nums = [1, 2, 3, 4]
solution = Solution()
print(solution.productExceptSelf(nums))
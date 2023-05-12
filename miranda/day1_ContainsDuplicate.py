from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))

#driver code
nums = [1, 2, 3, 3]
solution = Solution()
print(solution.containsDuplicate(nums))
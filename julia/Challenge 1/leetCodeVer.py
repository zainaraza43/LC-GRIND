# Challenge 1 - Contains Duplicate
# Author: Julia Sabelli
# LEETCODE VERSION

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        length = len(nums)
        for i in range(length - 1):
            if (i == (length - 1)) and (nums[i] != nums[i + 1]):
                return False
            elif (i != (length - 1)) and (nums[i] != nums[i + 1]):
                i += 1
                continue
            elif nums[i] == nums[i + 1]:
                return True

        return False


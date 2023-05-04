class Solution(object):
    def containsDuplicate(self, nums):
        nums_set = set(nums)
        if len(nums) != len(nums_set):
            return True
        return False 
            
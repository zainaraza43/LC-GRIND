class Solution(object):
    def containsDuplicate(self, nums):
        original_size = len(nums)
        new_set = {'l'}
        for num in nums:
            new_set.add(num)
        if original_size != len(new_set)-1:
            return True
        return False
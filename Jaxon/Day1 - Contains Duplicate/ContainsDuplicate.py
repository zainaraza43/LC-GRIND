class Solution(object):
    def containsDuplicate(self, nums):
        seen_vals = []
        for val in range(len(nums)):
            counter = 0
            for num in nums:
                if num == nums[val]:
                    counter += 1
            if counter > 1:
                return True
        return False 

            

            
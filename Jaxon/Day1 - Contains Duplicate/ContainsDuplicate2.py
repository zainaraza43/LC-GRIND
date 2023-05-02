class Solution(object):
    def containsDuplicate(self, nums):
        seen_vals = []
        for val in nums:
            if val not in seen_vals:
                seen_vals.append(val)
            else: return True
        return False


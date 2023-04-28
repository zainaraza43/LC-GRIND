# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

import array

class Solution(object):
    def containsDuplicate(self, nums):
        self.check = set()
        for number in nums:
            if number in self.check:
                return True
            else:
                self.check.add(number)
        return False

# Explanation
# I started off first by creating a new set 
# Then I made a for loop that loops over each number in nums
# If the number was found in the set that I created (meaning it was added previously in the for loop), we return True 
# If the number was not found, we add it to the set
# If no number is found twice, we return False

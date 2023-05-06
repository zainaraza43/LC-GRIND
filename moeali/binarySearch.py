# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.

class Solution(object):
    def search(self, nums, target):
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = (start + end)//2 
            if nums[mid] == target: 
                return mid
            elif nums[mid] < target: 
                start = mid + 1
            else: 
                end = mid - 1
        return -1

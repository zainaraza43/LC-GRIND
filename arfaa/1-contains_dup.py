"""
Contains Duplicate
May 3, 2023
https://leetcode.com/problems/contains-duplicate/

O(1) time? doubt. im bad at time complexity ;-;
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        return True
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        indicesList = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    if nums[i] + nums[j] == target:
                        indicesList.append(i)
                        indicesList.append(j)
                        return indicesList

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Time complexity: O(n)
        # Space complexity: O(n)

        prevNumbers = {} 
        for idx, num in enumerate(nums):
            difference = target - num 
            if difference in prevNumbers:
                return [prevNumbers[difference], idx]
            prevNumbers[num] = idx
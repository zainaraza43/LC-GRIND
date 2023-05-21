class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}
        for i, num in enumerate(nums):

            if (target - num) in hashmap:
                return [i,hashmap[target-num]]
                
            hashmap[num] =  i

            
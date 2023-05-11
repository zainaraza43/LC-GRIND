class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dic = {}
        
        for i in range(len(nums)):
            if nums[i] not in dic.keys():
                dic[target - nums[i]] = i
            else:
                return [dic[nums[i]], i]
    
    
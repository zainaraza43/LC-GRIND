class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        
        for i in range(len(nums)):
            n = target - nums[i]
            if n in map:
                return [map[n], i]
            map[nums[i]] = i  #not sure if there is a better way than this
 
 
            
            
            
            
                
        
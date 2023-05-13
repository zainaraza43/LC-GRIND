from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0)+1
        
        for k,v in counts.items():
            if v == 1:
                return k
        return -1

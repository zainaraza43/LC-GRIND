from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max = 0

        for num in nums:
            if num - 1 in numSet:
                continue
            
            seqLen = 1
            nextNum = num + 1
            while (nextNum in numSet):
                seqLen += 1
                nextNum += 1

            if (seqLen > max):
                max = seqLen
        
        return max
    
nums = [100,4,200,1,3,2]
solution = Solution()
print(solution.longestConsecutive(nums))
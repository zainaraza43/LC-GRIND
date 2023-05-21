from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [ [] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, f in count.items():
            freq[f].append(num)

        retVal = []
        for f in reversed(freq):
            for c in f:
                retVal.append(c)

                if (len(retVal) == k):
                    return retVal


nums = [3, 6, 10, 4, 9, 3, 6]
k = 2
solution = Solution()
print(solution.topKFrequent(nums, k))
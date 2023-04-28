from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            seen[n] = seen.get(n, i)

            if seen.get(target - n, None) is not None and seen[target - n] != i:
                return [seen[target - n], i]
        return [-1, -1]

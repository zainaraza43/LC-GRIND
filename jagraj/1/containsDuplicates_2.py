from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
            if count[n] == 2:
                return True
        return False

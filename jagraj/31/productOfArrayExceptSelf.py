from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        r: List[int] = [1]

        # Store product for every number BEFORE i
        for i in range(1, n):
            r.append(r[i - 1] * nums[i - 1])

        # Same thing but for everything AFTER i
        rightProd = 1
        for i in range(n - 2, -1, -1):
            rightProd *= nums[i + 1]
            r[i] *= rightProd

        return r

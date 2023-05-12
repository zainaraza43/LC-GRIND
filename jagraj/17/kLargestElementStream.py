from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.nums.sort()
        self.k = k

    def add(self, val: int) -> int:
        if not self.nums or val >= self.nums[-1]:
            self.nums.append(val)
            return self.nums[-self.k]
        if val <= self.nums[0]:
            self.nums.insert(0, val)
            return self.nums[-self.k]

        l = 0
        r = len(self.nums)
        m = (l+r)//2
        while True:
            if self.nums[m] <= val <= self.nums[m+1]:
                self.nums.insert(m+1, val)
                break
            if val < self.nums[m]:
                r = m
            else:
                l = m
            m = (r+l)//2
        return self.nums[-self.k]
        


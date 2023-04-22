from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    diffs = {}
    for i, n in enumerate(nums):
        if target - n in diffs:
            return [i, diffs[target - n]]
        diffs[n] = i

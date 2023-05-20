# Challenge 3 - Two Sum
# Author: Julia Sabelli
# IDE VERSION


from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    num_map = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

    return []


class Solution:

    if __name__ == '__main__':

        print("Testcase 1 = ", twoSum([2, 7, 11, 15], 9))
        print("\nTestcase 2 = ", twoSum([3, 2, 4], 6))
        print("\nTestcase 3 = ", twoSum([3, 3], 6))


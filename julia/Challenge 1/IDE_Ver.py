# Challenge 1 - Contains Duplicate
# Author: Julia Sabelli
# IDE VERSION

from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    nums.sort()
    length = len(nums)
    for i in range(length - 1):
        if (i == (length - 1)) and (nums[i] != nums[i + 1]):
            return False
        elif (i != (length - 1)) and (nums[i] != nums[i + 1]):
            i += 1
            continue
        elif nums[i] == nums[i + 1]:
            return True

    return False


class Solution:

    if __name__ == '__main__':

        print("Testcase 1 = ", containsDuplicate([1, 2, 3, 1]))
        print("\nTestcase 2 = ", containsDuplicate([1, 2, 3, 4]))
        print("\nTestcase 3 = ", containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

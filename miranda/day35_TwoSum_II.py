from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while (left < right):
            sum = numbers[left] + numbers[right]

            if (sum < target):
                left += 1
            if (sum > target):
                right -= 1
            if (sum == target):
                return [left + 1, right +1]

    
nums = [2, 3, 4]
target = 6
solution = Solution()
print(solution.twoSum(nums, target))
class Solution(object):
    def missingNumber(self, nums):
        return sum(list(range(0, len(nums) + 1))) - sum(nums)

nums = [3, 0, 1]
solution = Solution()
print(solution.missingNumber(nums))
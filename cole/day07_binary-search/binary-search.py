# the "fuck you it works" way
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.index(target) if target in nums else -1


# the "proper" way
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1
        if nums[0] == target:
            return nums[0]
        if nums[-1] == target:
            return len(nums) - 1
        mid = len(nums) // 2
        while lo != hi and nums[mid] != target:
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
            mid = (lo + hi) // 2
        return mid if nums[mid] == target else -1

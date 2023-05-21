class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1

        # very cursed but accounts for zeros
        zeros = nums.count(0)
        if zeros:
            out = [0 for _ in nums]
            if zeros > 1:
                return out
            for i, num in enumerate(nums):
                if num != 0:
                    product *= num
                else:
                    zeros = i
            out[zeros] = product
            return out

        # O(1) extra space, linear time
        for num in nums[1:]:
            product *= num
        out = [product]
        for x, y in zip(nums[:-1], nums[1:]):
            product //= y
            product *= x
            out.append(product)
        return out

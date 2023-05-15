from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        placeholder = 10 ** (len(digits)-1)
        total = 0
        for num in digits:
            total += num * placeholder
            placeholder //= 10

        total += 1
        retArray = [int(x) for x in str(total)]
        return retArray

digits = [9, 9]
solution = Solution()
print(solution.plusOne(digits))
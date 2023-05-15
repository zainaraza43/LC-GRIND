# you already saw the optimal C solution, now prepare yourself for the "fuck you" python solution
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(map(int, [*str(int("".join(map(str, digits))) + 1)]))

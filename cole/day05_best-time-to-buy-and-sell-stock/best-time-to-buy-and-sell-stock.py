# beats 98.22%

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestDiff = 0
        bestStart = prices[0]
        for day in prices[1:]:
            if day - bestStart > bestDiff:
                bestDiff = day - bestStart
            if day < bestStart:
                bestStart = day
        return bestDiff
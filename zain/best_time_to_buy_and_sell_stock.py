from typing import List


def maxProfit(self, prices: List[int]) -> int:
    l, maxProfit = 0, 0
    for r in range(1, len(prices)):
        if prices[r] < prices[l]:
            l = r
        else:
            maxProfit = max(maxProfit, prices[r] - prices[l])
    return maxProfit

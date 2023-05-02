class Solution:
    def maxProfit(self, prices):
        med = len(prices) // 2
        left = prices[:med]
        right = prices[med:]
        return max(self.maxProfit(left), self.maxProfit(right), max(right) - min(left)) if len(prices) > 1 else 0
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        max_profit = 0
        sell = 1

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                max_profit = max(prices[sell] - prices[buy], max_profit)
            else:
                buy = sell

            sell += 1

        return max_profit


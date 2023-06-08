# Challenge 5 - Best Time to Buy and Sell Stock
# Author: Julia Sabelli
# LEETCODE VERSION

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = 10e4
        maximum = 0
        maxprof = 0

        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]

            if prices[i] > minimum:
                maximum = prices[i]
                profit = maximum - minimum

                if maxprof < profit:
                    maxprof = profit

        return maxprof
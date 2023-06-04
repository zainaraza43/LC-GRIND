# Challenge 5 - Best Time to Buy and Sell Stock
# Author: Julia Sabelli
# IDE VERSION

from typing import List


def maxProfit(prices: List[int]) -> int:
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


class Solution:

    if __name__ == '__main__':

        print(maxProfit([7, 6, 4, 3, 1]))
        
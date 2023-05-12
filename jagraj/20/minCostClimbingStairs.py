from typing import List


class Solution:
    def __init__(self):
        self.poopy = []

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        self.poopy.append(cost[0])
        self.poopy.append(cost[1])

        for i in range(2, len(cost)):
            self.poopy.append(min(cost[i] + self.poopy[-1], cost[i] + self.poopy[-2]))

        return min(self.poopy[-1], self.poopy[-2])

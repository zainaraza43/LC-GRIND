from heapq import heapify, heappop, heappush


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapify(stones)
        while len(stones) > 1:
            a = heappop(stones)
            b = heappop(stones)
            if a != b:
                heappush(stones, -abs(a - b))
        return -stones[0] if stones else 0

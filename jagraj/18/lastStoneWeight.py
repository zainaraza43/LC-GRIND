from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            z = x - y
            if z > 0:
                heapq.heappush(stones, -z)

        return 0 if not stones else -stones[0]


if __name__ == "__main__":
    s = Solution()

    inbputs = [[2, 7, 4, 1, 8, 1]]
    for i in inbputs:
        print(i, s.lastStoneWeight(i))

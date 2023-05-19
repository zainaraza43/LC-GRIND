from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1

        j = list(zip(counts.keys(), counts.values()))
        j.sort(key=lambda x: x[1])

        print(j)
        return [i[0] for i in j[-k:]]


if __name__ == "__main__":
    s = Solution()

    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))

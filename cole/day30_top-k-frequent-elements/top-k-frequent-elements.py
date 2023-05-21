class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        return [k for k, v in sorted(Counter(nums).items(), key=lambda x: x[1], reverse=True)[:k]]
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        counts = defaultdict(list)
        for s in strs:
            counts[tuple(sorted(s))].append(s)
        return list(counts.values())

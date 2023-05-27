from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d: dict[str, List[str]] = {}
        for word in strs:
            s: str = "".join(sorted(word))
            d[s] = [*d.get(s, []), word]
        return list(d.values())

from collections import defaultdict


def isAnagram(self, s: str, t: str) -> bool:
    s_count = defaultdict(int)
    t_count = defaultdict(int)

    for c in s:
        s_count[c] += 1

    for c in t:
        t_count[c] += 1

    return s_count == t_count

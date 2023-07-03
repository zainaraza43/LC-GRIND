from collections import defaultdict


def binary_search(target: int, arr: list, key: callable = None):
    if len(arr) == 0:
        return -1
    if key is None:
        key = lambda x: x
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        m = (lo + hi) // 2
        if key(arr[m]) == target:
            lo = hi = m
        elif key(arr[m]) > target:
            hi = m
        else:
            lo = m + 1
    return lo if key(arr[lo]) <= target else lo - 1


class TimeMap:
    def __init__(self):
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        k = self.keys[key]
        i = binary_search(timestamp, k, lambda x: x[0])
        return k[i][1] if i != -1 else ""

    # Your TimeMap object will be instantiated and called as such:
    # obj = TimeMap()
    # obj.set(key,value,timestamp)
    # param_2 = obj.get(key,timestamp)

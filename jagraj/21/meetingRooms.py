from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        intervals.sort(key=lambda x: x.start)
        for i, k in enumerate(intervals[:-1]):
            if k.end > intervals[i + 1].start:
                return False

        return True


if __name__ == "__main__":
    s = Solution()

    print(s.can_attend_meetings([Interval(0, 30), Interval(5, 10), Interval(15, 20)]))
    print(s.can_attend_meetings([Interval(5, 8), Interval(9, 15)]))

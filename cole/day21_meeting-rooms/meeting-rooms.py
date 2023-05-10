from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        intervals = sorted(intervals, key=lambda x: x.start)
        for a, b in zip(intervals[:-1], intervals[1:]):
            if a.end > b.start:
                return False
        return True
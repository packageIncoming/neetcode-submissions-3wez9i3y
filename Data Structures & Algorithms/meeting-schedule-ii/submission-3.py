"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        starts.sort()
        ends.sort()
        endPtr = 0
        startPtr = 0
        res=0
        count=0
        while startPtr < len(starts) and endPtr < len(ends):
            while startPtr < len(starts) and starts[startPtr] < ends[endPtr]:
                count+=1
                startPtr+=1
            res=max(count,res)
            count-=1
            endPtr+=1

        return res
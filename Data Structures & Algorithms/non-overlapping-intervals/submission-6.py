class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res=0
        intervals = sorted(intervals)
        print(intervals)
        last_end=intervals[0][1]
        for i in range(1,len(intervals)):
            if intervals[i][0] < last_end:
                res+=1
                last_end = min(last_end,intervals[i][1])
            else:
                last_end = max(last_end,intervals[i][1])
        return res
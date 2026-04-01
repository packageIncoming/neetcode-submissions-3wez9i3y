class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        res=0
        i=0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]: # iterate over remaining intervals
            if start >= prevEnd: # if the next interval starts beyond the current ending
                prevEnd  = end #    then just set the ending 
            else:
                res+=1  #otherwise there is an overlap
                prevEnd = min(end,prevEnd)  # update the overlap to be the minimum of the three (lowest overlap)
        return res
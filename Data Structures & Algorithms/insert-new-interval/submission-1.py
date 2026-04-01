'''
Idea:
    -newInterval overlaps if its start falls between the start and end of some existing interval


'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            # add all the intervals whose ending values are less than the new interval's start (can't overlap)
            output.append(intervals[i])
            i+=1
        if i < len(intervals):
            # this means there's more to go
            # at this point we know that intervals[i] has an ending value either greater than or equal to 
            # the new interval's start 
            # there are two cases from here
            # 1. the start of intervals[i] is greater than the end of newInterval
            # meaning there is NO OVERLAP
            if intervals[i][0] > newInterval[1]:
                output.append(newInterval) # add the new interval
                while i < len(intervals): # then add all the other intervals
                    output.append(intervals[i])
                    i+=1
            else:
                # 2. the start of the interval is less than or equal to the end of the new interval
                # meaning the new interval starts somewhere in intervals[i]
                # meaning they can be merged
                # but this can continue on beyond just a single loop so it needs to be done while this condition
                # is true
                while i < len(intervals) and intervals[i][0] <= newInterval[1]:
                    curr = intervals[i]
                    newInterval = [min(curr[0],newInterval[0]),max(curr[1],newInterval[1])]
                    i+=1
                output.append(newInterval) # add the new interval
                while i < len(intervals): # then add all the other intervals
                    output.append(intervals[i])
                    i+=1
        elif i == len(intervals):
            output.append(newInterval)
        return output
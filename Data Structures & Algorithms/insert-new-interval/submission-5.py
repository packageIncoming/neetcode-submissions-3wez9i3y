'''
    The intervals are already sorted so when a new interval is added
at most 3 will be merged

    when do you merge an interval?

    If they are sorted then the numbers are always increasing
so if you add then that would mean that the 'left' (current) interval
ends after the inserted interval starts, and the 'right' (next) interval
starts before the inserted interval ends


this assumption was false.



'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res=[]
        
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0],intervals[i][0]),
                    max(newInterval[1],intervals[i][1])
                ]
        res.append(newInterval)
    
        return res


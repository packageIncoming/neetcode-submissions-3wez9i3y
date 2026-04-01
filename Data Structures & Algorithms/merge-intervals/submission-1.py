class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # two intervals [s1,e1] and [s2,e2] overlap IFF s2<=e1 AND s1<=e2
        intervals = sorted(intervals, key=lambda x: x[0])
        output = []
        focusPtr = 0
        while focusPtr < len(intervals):
            focusInterval = intervals[focusPtr]
            mergePtr = focusPtr+1
            while mergePtr < len(intervals):
                mergable = intervals[mergePtr]
                if focusInterval[0] <= mergable[1] and mergable[0] <= focusInterval[1]:
                    focusInterval = [min(focusInterval[0],mergable[0]),max(focusInterval[1],mergable[1])]
                else:
                    break
                mergePtr+=1
            output.append(focusInterval)
            focusPtr=mergePtr

                    
                


        return output
'''
Idea:
Initialize a dictionary, changesDict, where key=KM east, values=changes made at that stop (arr of ints)

'''

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changesDict = defaultdict(list)
        start=float('inf')
        end=float('-inf')
        for trip in trips:
            change = trip[0]
            add = trip[1]
            leave = trip[2]
            changesDict[add].append(change)
            changesDict[leave].append(-change)
            start = min(start,add,leave)
            end = max(end,add,leave)
        
        curCapacity=0
        for i in range(start,end+1):
            changes = changesDict[i]
            for change in changes:
                curCapacity += change
                if curCapacity > capacity:
                    return False
        return True
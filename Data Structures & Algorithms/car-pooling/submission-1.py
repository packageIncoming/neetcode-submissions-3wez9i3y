'''
Idea:
Initialize a dictionary, changesDict, where key=KM east, values=changes made at that stop (arr of ints)

'''

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changesArr = []
        for trip in trips:
            change = trip[0]
            add = trip[1]
            leave = trip[2]
            changesArr.append([add,change])
            changesArr.append([leave,-change])

        changesArr.sort()
        curCapacity=0

        for change in changesArr:
            curCapacity += change[1]
            if curCapacity > capacity:
                return False
        return True
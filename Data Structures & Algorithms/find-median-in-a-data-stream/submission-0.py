class MedianFinder:

    def __init__(self):
        self.vals = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.vals,num)

    def findMedian(self) -> float:
        seen = []
        res=None
        if len(self.vals)%2==1:
            #odd
            median = len(self.vals)//2
            for i in range(median+1):
                seen.append(heapq.heappop(self.vals))
            res = seen[-1]
        else:
            #even
            median = len(self.vals)//2
            for i in range(median+1):
                seen.append(heapq.heappop(self.vals))
            res =( seen[-1] + seen[-2] )/ 2
        # reinsert
        for v in seen:
            self.addNum(v)
        return res

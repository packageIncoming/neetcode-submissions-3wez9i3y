'''
2 heaps, one with the smaller half of values, one with the larger half of values
smallHeap <= largeHeap
smallHeap = maxHeap
largeHeap = minHeap
len(smallHeap) ~= len(largeHeap)
diff of lengths greater than 1 => pop from larger heap and push to smaller heap

if len smallheap > len largeHeap then the array length is odd and the median is smallHeap[0]
if len largeHeap > len smallHeap then arr len is odd and median is largeHeap[0]
if arr len is even then the median is (smallHeap[0] + largeHeap[0]) / 2

by default add to smallHeap
If the max of smallHeap > min of largeHeap then pop from small push to large
Rebalance heaps if len difference is greater than 1
'''
class MedianFinder:

    def __init__(self):
        self.smallHeap = []
        self.largeHeap = []


    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap,-num) # smallheap = maxHeap => all elems are negative
        if self.largeHeap and -self.smallHeap[0] > self.largeHeap[0]:
            # top value too large, pop from small push to large
            top = -heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap,top)
        if len(self.smallHeap) > len(self.largeHeap) + 1:
            # small has too many elements, pop from small push to large
            top = -heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap,top)
        elif len(self.largeHeap) > len(self.smallHeap) + 1:
            # large has too many elements, pop from large push to small
            top = -heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap,top)

    def findMedian(self) -> float:
        totalLength = len(self.smallHeap) + len(self.largeHeap)
        if totalLength%2 == 0:
            # even, need to average tops and return as median
            return (-self.smallHeap[0] + self.largeHeap[0]) / 2
        else:
            # odd; get top elem from larger heap
            if len(self.smallHeap) >= len(self.largeHeap):
                return -self.smallHeap[0]
            else:
                return self.largeHeap[0]
        
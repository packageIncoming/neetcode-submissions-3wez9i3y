from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False # can't evenly divide into groups of groupSize
        hmap = Counter(hand)
        minHeap = []
        for num in hmap.keys():
            heapq.heappush(minHeap,num)
        
        while minHeap:
            topValue = minHeap[0]
            for i in range(topValue,topValue+groupSize):
                if i not in hmap or hmap[i] <= 0:
                    return False
                hmap[i]-=1
                if hmap[i] == 0:
                    if i != minHeap[0]:
                        return False
                    else:
                        heapq.heappop(minHeap)

        return True
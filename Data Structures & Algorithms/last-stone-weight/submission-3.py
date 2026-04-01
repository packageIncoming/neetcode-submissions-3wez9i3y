'''
You are given an array of integers stones where stones[i] represents the weight of the ith stone.
    - Not fed other inputs, this is the only input given
    
We want to run a simulation on the stones as follows:
    - main program loop:
At each step we choose the two heaviest stones, with weight x and y and smash them together
    -Need some method for collecting the two heaviest stones
    - Already know that I will be using a heap for this but will it be min or max heap??
If x == y, both stones are destroyed
    - Case 1, maxes are the same, remove both from heap
If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
    - Case 2, one stone is heavier than the other, subtract heavier-lighter, append new stone to heap
Continue the simulation until there is no more than one stone remaining.
    - Repeat until len of heap is <=1
Return the weight of the last remaining stone or return 0 if none remain.
    -Return heap[0] if len(heap) >0 else return 0

Example Walkthrough
stones = [2,3,6,2,4]
1. pop 6 and 4, smash and left with 2, append 2 
1r. stones = [2,3,2,2] (6 and 4 removed, replaced with a 2)
2. pop 3 and 2, smash and left with 1 , stones = [1,2,2]

* Need to use maxheap
    - 1 <= stones[i] <= 100 so we can invert before adding, then invert on use to get original value

Generalization:
1. result = pop() - pop()
2. if abs(result) > 0, append(result)
3. else, continue 
4. return heap[0] if len(heap) > 0 else return 0
'''

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones = list(-stone for stone in stones)
        heapq.heapify(stones)
        while len(stones) > 1:
            val1 = -1*heapq.heappop(stones)
            val2 = -1*heapq.heappop(stones)
            if val1 > val2:
                heapq.heappush(stones,-(val1-val2))
            elif val2 > val1:
                heapq.heappush(stones,-(val2-val1))
        return -stones[0] if len(stones) > 0 else 0
        
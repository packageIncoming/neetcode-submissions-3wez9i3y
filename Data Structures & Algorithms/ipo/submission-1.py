'''
Start off with w capital, goal is to maximize it within k distinct projects
    -cannot reuse projects
To finish a project i, you need to have w>=capital[i]. When it's done, w = w+ profits[i]
k is how many you can pick at most but there is the possibility that you WONT get k projects
    -k is the upper limit

How would I solve this as a human?
Input: k = 3, w = 0, profits = [1,4,2,3], capital = [0,3,1,1]
1.
    Only project I can choose is i=0
        Now k=2,w=1
    With w=1, I can choose i=2 or i=3. i=3 has more profit so I choose that one
        Now k=1,w=4
    The highest profit project I can choose is i=1 so I choose that one
        Now k=0,w=8 and I am done
What did I do?
    -Find the highest profit project with capital <=w
    -Order did not matter and the potential answer was updated whenever I chose a project
        -So a data structure with a rigid order probably wouldn't work

This is closest in design to a MinHeap of tuples (capital,profit)

Steps:
    1. Make pairs then Heapify
        -Top values will be the least expensive to execute
    2. While the heap is not empty and the top of the heap has capital <= w, pop 
        -Add these to a maxHeap of potential picks
    3. If there is no item in the potential picks then return the current profit (can't add any more)
    4. If there is a most profitable then add its profit and decrement k
    5. Repeat steps 2 thru 4 until k=0 or 3 met
    6. return w
'''

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        remaining=k
        mProfit=w
        # Pairs then heapify
        heap = []
        for i in range(len(profits)):
            heap.append((capital[i],profits[i]))
        heapq.heapify(heap)
        potentialPicks = [] # MAXHEAP of (-profit,capital)
        while remaining > 0:

            while heap and heap[0][0] <=mProfit:
                top = heapq.heappop(heap)
                newTop = (-top[1],top[0])
                heapq.heappush(potentialPicks,newTop)
            if not potentialPicks:
                return mProfit
            else:
                bestItem = heapq.heappop(potentialPicks)
                mProfit += -bestItem[0]
                remaining-=1

        return mProfit

        
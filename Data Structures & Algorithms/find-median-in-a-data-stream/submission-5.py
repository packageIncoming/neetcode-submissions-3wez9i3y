'''
Median would be at the middle

How can you split something in half while keeping order?
Minheap and Maxheap?
Minheap for righthand side so that the value is the smallest large value
Maxheap for lefthand side so that the value is the largest small value

The problem is in deciding which side to put elements at a time

Lets say that for an odd number of elements we want the median to be in the left
For an even number of elements we want the avg of the two middle values

If the left has 2 and the right has 3 there are 5 elements the median is the largest
    on the lefthand side

if the left has 3 and the right has 3 there are 6 elements the median is the avg of l and r



So the lengths of the right and left cannot be more than 1 apart at any time

How do you decide where to add?
We can default to adding to the left. Then, if the top value on the left is >= top
value in the right, we pop and move it over to the right

There also needs to be a step of re-balancing at the end, ensure lengths are within 1 of eachother






'''

class MedianFinder:

    def __init__(self):
        self.left = [] # MAXHEAP
        self.right = [] # MINHEAP
        

    def addNum(self, num: int) -> None:
        if self.right and num > self.right[0]:
            heapq.heappush(self.right,num)
        else:
            heapq.heappush(self.left,-num)

        if len(self.left) > len(self.right)+1:
            top = -heapq.heappop(self.left) # NEGATIVE SINCE GOING FROM MAX->MINHEAP
            heapq.heappush(self.right,top)

        if len(self.right) > len(self.left)+1:
            # Rebalance other way
            top = -heapq.heappop(self.right)
            heapq.heappush(self.left,top)

        

    def findMedian(self) -> float:
        if len(self.left)>len(self.right):
            return -self.left[0]
        elif len(self.left)<len(self.right):
            return self.right[0]
        else:
            return (-self.left[0] + self.right[0])/2
        
        
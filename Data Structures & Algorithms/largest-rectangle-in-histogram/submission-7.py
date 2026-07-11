'''
properties that must be followed:

the rectangles must be continuous (no gaps)
If you are given a continuous section of the histogram, the width
is len(section) and the height is min(section),
    thus the area is len(section)*min(section)

BRUTE FORCE:
start from every bar, iterate left to right calculating the area.
When you get to a new rectangle, calculate the minimum & then the area
up to that point, then update the global max area
O(n^2) time complexity O(1) space


example

[1,3,7]
[1]->1
[1,3]->2
[1,3,7]->3
[3]->3
[3,7]->6
[7]->7

Is there a solution better than O(n^2)?
Cannot modify ordering of original heights

When you get to a new bar you can either add it to your existing rectangle
or you can start anew
So is it greedy then?




'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res=0

        for i in range(len(heights)):
            curH = heights[i]
            for j in range(i,len(heights)):
                width = (j-i)+1
                curH = min(curH,heights[j])
                res = max(res, width * curH)

        return res
        
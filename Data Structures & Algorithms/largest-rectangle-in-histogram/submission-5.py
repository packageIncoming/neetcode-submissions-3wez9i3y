class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1: return heights[0]
        area = heights[0]
        for i in range(len(heights)):
            barHeight = heights[i]
            width = 1
            for j in range(i-1,-1,-1):
                if heights[j] < heights[i]:
                    break
                width+=1
            for j in range(i+1,len(heights)):
                if heights[j] < heights[i]:
                    break
                width+=1
            area= max(area, barHeight*width)
        return area
            
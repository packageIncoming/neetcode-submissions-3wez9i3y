class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1: return heights[0]

        area = 0
        stack = [] # index, height pairs
        for i,h  in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx,height = stack.pop()
                area = max(area, (height * (i-idx)))
                start=idx
            stack.append([start,h])
        for i, h in stack:
            area = max(area, h * (len(heights)-i))

        return area
            
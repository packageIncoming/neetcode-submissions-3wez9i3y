class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #solution 1, brute force solution
        #iterate over every possible combination and return the max
        # O(n^2) time complexity
        highest_area=-1
        for i in range(len(heights)):
            for j in range (i+1,len(heights)):
                width = j-i
                height = min(heights[i],heights[j])
                area = width*height
                highest_area = max(area,highest_area)
        return highest_area
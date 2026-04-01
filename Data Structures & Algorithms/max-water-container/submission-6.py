class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights)-1
        cur_area = r* min(heights[l],heights[r])
        highest_area  = cur_area

        while l < r:
            cur_area = (r-l) * min(heights[l],heights[r])
            highest_area = max(cur_area,highest_area)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1

        return highest_area
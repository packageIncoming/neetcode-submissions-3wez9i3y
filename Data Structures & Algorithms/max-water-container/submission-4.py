class Solution:
    def area(self, arr, l_ptr,r_ptr):
        return (r_ptr - l_ptr) * min(arr[l_ptr],arr[r_ptr])

    def maxArea(self, heights: List[int]) -> int:
        #solution 2, optimized solution
        # (?): Start on left and right and move inwards 
        # O(n) time complexity
        highest_area = -1
        l_ptr = 0
        r_ptr = len(heights)-1
        while l_ptr < r_ptr:
            cur_area = self.area(heights,l_ptr,r_ptr)

            highest_area = max(cur_area,highest_area)
            if heights[l_ptr] <= heights[r_ptr]:
                l_ptr+=1
            else:
                r_ptr -=1
        return highest_area
            


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
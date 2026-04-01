class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0
        total_area = 0
        prefix_max = [0] * len(height)
        suffix_max =[0] * len(height)
        # Construct prefix maxes
        cur_max = 0
        for i in range(1,len(height)):
            cur_max = max(cur_max,height[i-1])
            prefix_max[i] = cur_max
        # Construct suffix maxes
        cur_max = 0
        for i in range(len(height)-2,-1,-1):
            cur_max = max(cur_max,height[i+1])
            suffix_max[i] = cur_max
        for i in range(len(height)):
            area = min(prefix_max[i],suffix_max[i]) - height[i]
            print(i,area)
            if area > 0:
                total_area+=area
        return total_area
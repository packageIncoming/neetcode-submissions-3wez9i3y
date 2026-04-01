class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxes = []
        chunks = []
        l = 0
        for r in range(len(nums)):
            if (r-l)+1 > k:
                l+=1
            if (r-l)+1 == k:
                chunks.append(nums[l:r+1])
        for chunk in chunks:
            cur_max = float('-inf')
            for val in chunk:
                cur_max = max(cur_max,val)
            maxes.append(cur_max)
        return maxes
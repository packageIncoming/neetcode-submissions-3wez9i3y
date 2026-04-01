class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxes = []
        chunks = []
        l = 0
        curMax = float('-inf')
        for r in range(len(nums)):
            
            if (r-l)+1 > k:
                if nums[l] == curMax:
                    #print(f"dropped off maximum: {curMax}")
                    curMax = float('-inf')
                    for i in range(l+1,r):
                        curMax = max(curMax,nums[i])
                l+=1
            curMax = max(curMax,nums[r])
            if (r-l)+1 == k:
                maxes.append(curMax)

        return maxes
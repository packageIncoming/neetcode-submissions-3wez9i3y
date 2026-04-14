class Solution:
    def rob(self, nums: List[int]) -> int:
        dp0 = 0
        dp1 = 0
        for i in range(len(nums)-1,-1,-1):
            skipCur = dp0
            takeCur = nums[i] + dp1
            dp1=dp0
            dp0  = max(skipCur,takeCur)

        
        return dp0
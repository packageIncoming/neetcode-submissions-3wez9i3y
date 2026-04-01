class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')]*(len(nums))
        dp[len(nums)-1] = 0
        for i in range(len(nums)-2,-1,-1):
            jDist = nums[i]
            for j in range(i+1,min(len(nums),i+jDist+1)):
                dp[i] = min(dp[i],dp[j])
            dp[i]+=1             
        return dp[0]
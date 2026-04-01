class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = [False]*(len(nums))
        memo[len(nums)-1] = True
        for i in range(len(nums)-1,-1,-1):
            jDist = nums[i]
            for j in range(i+1,i+jDist+1):
                memo[i] = memo[i] or memo[j]
                if memo[i] is True:
                    break
        return memo[0]


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False]* len(nums)
        dp[-1] =True

        for dp_idx in range(len(nums)-2,-1,-1):
            num= nums[dp_idx]
            for j in range(num):
                nxt_idx = j+dp_idx+1
                if nxt_idx < len(nums) and dp[nxt_idx] is True:
                    dp[dp_idx]= True
                    break

        return dp[0]        
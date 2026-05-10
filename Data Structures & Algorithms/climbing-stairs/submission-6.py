class Solution:
    def climbStairs(self, n: int) -> int:
        dp0 = 1
        dp1 = 0
        for i in range(n):
            cur = dp0+dp1
            dp1=dp0
            dp0=cur
        return dp0
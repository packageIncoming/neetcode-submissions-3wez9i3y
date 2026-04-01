class Solution:
    def climbStairs(self, n: int) -> int:
        self.ways = 0
        def permute(n):
            if n == 0:
                self.ways+=1
                return
            if n < 0:
                return
            permute(n-1)
            permute(n-2)
        permute(n)
        return self.ways

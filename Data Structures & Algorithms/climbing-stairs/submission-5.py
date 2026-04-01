class Solution:
    
    def climbStairs(self, n: int) -> int:
        self.memo = {}
        def climb(n):
            if n <= 0: return 0
            if n == 1: return 1
            if n == 2: return 2
            if n in self.memo:
                return self.memo[n]
            self.memo[n] = climb(n-1) + climb(n-2)
            return self.memo[n]
        return climb(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.memo = {}

        def solve(i):
            if i in self.memo:
                return self.memo[i]
            if i >= len(cost):
                return 0
            self.memo[i] = cost[i] + min(solve(i+1),solve(i+2))
            return self.memo[i]
        
        return min(solve(0),solve(1))
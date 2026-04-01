class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = {0:0}
        def dfs(curAmount):
            # iterate back to front of the coins array with i, if curAmount-coins[i] == 0, return 1,
            # if curAmount-coins[i] > 0 then run dfs(curAmount) 
            # if curAmount-coins[i] < 0 then continue
            if curAmount in self.memo:
                return self.memo[curAmount]
            minimum = float('inf')
            for i in range(len(coins)-1,-1,-1):
                if curAmount-coins[i] == 0:
                    return 1
                elif curAmount-coins[i] > 0:
                    minimum = min(minimum,1+dfs(curAmount-coins[i]))
            self.memo[curAmount] = minimum
            return self.memo[curAmount]
        res = dfs(amount)
        if res == float('inf'):
            return -1
        else:
            return res                    
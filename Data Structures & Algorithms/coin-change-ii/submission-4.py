class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        useSet = set()
        cache = [[-1]*(amount+1) for i in range(len(coins)+1)] #key = [coin][amount]
        def dfs(i,curTot):

            if curTot == 0:
                return 1
            elif curTot < 0 or i >= len(coins):
                return 0
            if cache[i][curTot]!=-1:
                return cache[i][curTot]
            # decisions:
            # 1. use current coin
            #   1a. use current coin and keep i the same
            #   1b. use current coin and increment i
            useAndKeep = dfs(i,curTot-coins[i])
            useAndIncrement = dfs(i+1, curTot)
            cache[i][curTot]= useAndKeep + useAndIncrement 
            return cache[i][curTot]
        
        return dfs(0,amount)
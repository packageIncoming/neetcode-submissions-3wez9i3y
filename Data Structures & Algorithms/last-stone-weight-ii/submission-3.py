class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # knapsack
        tot = sum(stones)
        memo = [[-1 for i in range(tot+1)] for j in range(len(stones))]  #[i][curTot]
        targetValue = tot//2
        def search(i,curTot):
            nonlocal targetValue
            if curTot >= targetValue or i == len(stones):
                return abs(curTot - (tot - curTot))

            if memo[i][curTot] != -1:
                return memo[i][curTot]
            
            memo[i][curTot] = min(search(i+1,curTot),search(i+1,curTot+stones[i]))
            return memo[i][curTot]
        return search(0,0)
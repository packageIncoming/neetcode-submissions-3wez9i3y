class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # knapsack
        tot = sum(stones)
        memo = [[-1 for i in range(tot+1)] for j in range(len(stones))]  #[i][curTot]
        targetValue = tot//2
        closestValue = float('inf')
        def search(i,curTot):
            nonlocal closestValue
            nonlocal targetValue
            if i == len(stones):
                if abs(curTot-targetValue) < abs(closestValue-targetValue):
                    closestValue=curTot
                return curTot

            if memo[i][curTot] != -1:
                return memo[i][curTot]
            # choose not to include
            
            # choose to include
            
            memo[i][curTot] = min(search(i+1,curTot),search(i+1,curTot+stones[i]))
            return memo[i][curTot]
        res=search(0,0)
        print(res)
        otherPile = tot - closestValue
        return abs(otherPile-closestValue)
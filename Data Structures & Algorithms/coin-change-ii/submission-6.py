class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        bottomRow = [0]*(amount+1)
        bottomRow[amount]=1
        for coinIndex in range(len(coins)-1,-1,-1):
            topRow = [0]*(amount+1)
            topRow[amount]=1
            for curAmount in range(amount-1,-1,-1):
                newAmount = curAmount + coins[coinIndex]
                topRow[curAmount] = bottomRow[curAmount]
                if newAmount <= amount:
                    topRow[curAmount] += topRow[newAmount]
            bottomRow=topRow
        return bottomRow[0]
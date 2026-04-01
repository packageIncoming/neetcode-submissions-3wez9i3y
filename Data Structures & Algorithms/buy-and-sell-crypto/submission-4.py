class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1: return 0
        curProfit = float('-inf')
        curMin  = float('inf')
        for r in range(len(prices)):
            if prices[r] < curMin:
                curMin = prices[r]
            else:
                curProfit = max(curProfit, prices[r] - curMin)

        return max(0,curProfit)
'''
am i tweaking or is this greedy?

say you have [1,3,5]
if you buy @ 1 sell at @ 3 profit = 2
buy @ 1 sell @ 5-> profit = 4
buy @ 3 sell @ 5 -> profit=2
so it doesn't make a difference if you hold, just sell the moment you can & buy immediately

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0

        lastBuy = float('inf')
        for i in range(len(prices)):
            if prices[i] > lastBuy:
                profit += prices[i]-lastBuy
                lastBuy=prices[i]
            else:
                lastBuy = prices[i]

        return profit 
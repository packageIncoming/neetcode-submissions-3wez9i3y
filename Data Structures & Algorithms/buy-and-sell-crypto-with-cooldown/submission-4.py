'''
After you sell your NeetCoin, you cannot buy another one on the next day
- (i.e., there is a cooldown period of one day).

You may only own at most one NeetCoin at a time.
    -0/1 buy or sell mode


Example:
Input: prices = [1,3,4,0,4]

Output: 6


'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def findMaxProfitAtIndex(i,curBuyPrice):
            if i >= len(prices):
                return 0
            tag = (i,curBuyPrice)
            if tag in memo:
                return memo[tag]
            skip = findMaxProfitAtIndex(i+1,curBuyPrice)
            if curBuyPrice is None:
                # only option is to buy at the current point (cannot sell nothing)
                memo[tag] = max(skip,findMaxProfitAtIndex(i+1,prices[i]))
            else:
                # we can either decide to sell now or sell later
                sellNow = prices[i] - curBuyPrice
                memo[tag]= max(sellNow + findMaxProfitAtIndex(i+2,None),skip)
            return memo[tag]
        
        return findMaxProfitAtIndex(0,None)
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
        def findMaxProfitAtIndex(i,canBuy):
            if i >= len(prices):
                return 0
            tag = (i,canBuy)
            if tag in memo:
                return memo[tag]
            # we can either decide to buy later, sell later, buy now, or sell now
            # we can only buy now if we haven't bought (canBuy=True)
            # we can only sell now if we HAVE bought (canBuy=False)
            # in both scenarios we can skip
            skip = findMaxProfitAtIndex(i+1,canBuy) # carry state
            if not canBuy:
                #means we have bought so we can only sell
                sell = findMaxProfitAtIndex(i+2,not canBuy) + prices[i]
                memo[tag] = max(skip,sell)
            else:
                # means we have sold we can only buy
                buy = findMaxProfitAtIndex(i+1,not canBuy) - prices[i]
                memo[tag] = max(skip,buy)
            return memo[tag]
        return findMaxProfitAtIndex(0,True)
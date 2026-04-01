''' How would the recursion play out?:
Decisions at each price (i):
-   Buy at this price if not already bought
-   Sell at this price if already bought
-   Skip
-   Max profit at any point is either buy/sell at point OR skip

-   However we can sell and buy immediately
-   Buying and selling immediately makes no sense, that's just 0 profit (unneeded recursion)

Notes:
-   Prices are always >= 0 so can use -1 as placeholder
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # I think 2D Top-down recursion might be the best bet here
        memo = {}# first thought is to use 2d dict as memo
        def recurse(i,lastBought):
            if i >= len(prices):
                return 0 # base case
            tag = (i,lastBought)
            if tag in memo:
                return memo[tag]
            
            skip = recurse(i+1,lastBought) # do nothing
            # if lastBought is not -1 then that means we bought before so we can only sell now
            # if lastBought is -1 that means we have NOT  bought so we can only buy
            profit=0
            if lastBought != -1 :
                # if lastBought  
                profit = prices[i] - lastBought
                memo[tag] = max(skip,profit+recurse(i+1,-1),profit+recurse(i+1,prices[i]))
            elif lastBought == -1:
                # lastBought DNE so we can buy or skip now
                memo[tag] = max(skip,recurse(i+1,prices[i]))
            return memo[tag]

        return recurse(0,-1)
            
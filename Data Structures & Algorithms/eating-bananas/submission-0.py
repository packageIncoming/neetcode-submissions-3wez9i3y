class Solution:
    def timeForEatingRate(self,piles,eatingRate):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile/eatingRate)
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        fastestRate = max(piles)
        minRate = float('inf')
        l, r  = 1, fastestRate
        while l <= r:
            midRate = (l+r)//2
            timeForRate = self.timeForEatingRate(piles,midRate)
            #print(f"For rate {midRate} it would take {timeForRate} hours")
            if timeForRate <= h:
                minRate = min(midRate,minRate)
            # set new bounds
            # if time > h then rate needs to increase
            if timeForRate > h:
                l=midRate+1
            else:
                # otherwise if time <= h then we can try to find a slower rate
                r=midRate-1
        return minRate
'''
off the dome: koko eating bananas 
ITS AT LEAST K RIBBONS NOT AT MOST OR EXACTLY 

YOU CAN CUT ANY NUMBER OF TIMES OR NOT CUT AT ALL

What is the SMALLEST that you can cut
NOTHING (x=0)

What is the BIGGEST that you can cut
THE LOWEST VALUE IN ribbons[]
[9,7,5] can't cut 5 into 9 and 0

THE RANGE:
0 to MIN(ribbons)

THE VALIDATION FUNCTION:
Get your testing value,t
Iterate over all the lengths in ribbons[] and sum up:
    ribbons[i] // t for i in range(len(ribbons))
If that value == k exit early

If that value < k then that means the cut size is too big-> reduce t 
If that value > k then (update) & go upwards since you were able to cut more than needed
You are aiming to get the MAX LENGTH of AT LEAST K PIECES



'''

class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:

        def testValue(t):
            if t == 0:
                return k
            r = 0
            for i in range(len(ribbons)):
                r+= ribbons[i]//t
            return r

        lo,hi = 0, max(ribbons)
        res=0

        while lo <= hi:
            mid = int((lo+hi)/2)
            v = testValue(mid)
            if v < k:
                # not valid, too big
                hi=mid-1
            elif v >=k:
                res = max(res,mid)
                # try going higher
                lo=mid+1


        return res
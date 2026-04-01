class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 1, x
        cur=0
        while l <= r:
            mid = (l+r)//2
            if mid*mid == x:
                return mid
            elif mid*mid>x:
                # overshot
                r=mid-1
            elif mid*mid < x:
                # this will be the best fit
                cur=max(cur,mid)
                l=mid+1
        return cur
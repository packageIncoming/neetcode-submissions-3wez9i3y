class Solution:
    def reverse(self, x: int) -> int:
        maxnum = 2**31 - 1
        minnum = -(2**31)
        res=0
        sign = -1 if x<=0 else 1
        x = abs(x)
        places=int(math.log10(x)) if x > 0 else 0
        while x >0:
            rem = x % 10
            if rem >0:
                res+= rem * 10 **places
            places-=1
            x = x // 10
        res=res*sign
        if res >= maxnum or res <= minnum:
            return 0
        return res
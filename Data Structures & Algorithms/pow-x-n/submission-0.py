class Solution:
    def myPow(self, x: float, n: int) -> float:
        res=1
        val = x if n >=0 else 1/x
        for i in range(abs(n)):
            res*=val
        return res
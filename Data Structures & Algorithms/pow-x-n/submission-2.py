class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if x == 0: return 0 
        memo = {}
        memo[0]=1
        val = x if n >0 else 1/x
        def recursion(i):
            if i in memo:
                return memo[i]
            
            memo[i] = val*recursion(i-1)
            return memo[i]

        return recursion(abs(n))
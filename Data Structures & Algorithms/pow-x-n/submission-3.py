class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if x == 0: return 0 
        memo = {}
        memo[0]=1
        val = x if n >0 else 1/x
        memo[1] = val
        def recursion(i):
            if i in memo:
                return memo[i]
            
            if i%2==0:
                #even
                memo[i] = recursion(i//2) * recursion (i//2)
            else:
                # odd
                memo[i] = recursion(i//2) * recursion (i//2) * val
            return memo[i]

        return recursion(abs(n))
'''
First thoughts, seems like recursion + TOP-down DP perhaps 1D 
Lots of branches though, at an integer N you have 2 thru N to choose as the next multiple

Example walkthrough:
N=4
Res=1
Choose a number, i,  in range(2,N)
Remainder = N-i
Res = max(Res, i * recursion(N-i))
return Res

Base case:
N == 0 --> Return 1
N < 0 --> Return 0 (Since it's an invalid combination, went over)

Sum of k positive integers where k>=2 
    -> Means that there need to be at least 2 digits

'''


class Solution:
    def integerBreak(self, n: int) -> int:
        memo = [-1] * (n+1)

        def dfs(N,k):
            if N < 0 or N == 0 and k < 2:
                return 0
            elif N == 0:
                return 1
            if memo[N] != -1:
                return memo[N]
            res=1
            for i in range(1,N+1):
                res = max(res,i*dfs(N-i,k+1))
            memo[N] = res
            return memo[N]
        return dfs(n,0)
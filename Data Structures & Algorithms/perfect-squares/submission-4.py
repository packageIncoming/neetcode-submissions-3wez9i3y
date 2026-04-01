class Solution:
    def numSquares(self, n: int) -> int:
        #   start= closest perfect square
        memo = [-1]*(n+1)
        def solve(value):
            if value == 0:
                return 0 # solved
            if memo[value]!=-1:
                return memo[value]
            res=value

            for i in range(1,value+1):

                if i*i > value: break
                res = min(res,1+ solve(value-(i*i)))


            memo[value]=res
            return memo[value]
        return solve(n)
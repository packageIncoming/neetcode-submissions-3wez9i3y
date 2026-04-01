class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {
            0:0,
            1:1,
            2:1
        }
        def recurse(i):
            if i in memo:
                return memo[i]
            memo[i] = recurse(i-3) + recurse(i-2) + recurse(i-1)
            return memo[i]
        return recurse(n)
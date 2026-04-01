

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0]*(len(t)+1) for _ in range(len(s)+1)] #[s][t]
        dp[len(s)][len(t)] = 1 # only 1 way to make string "" using "" (absolute base case)
        # Table rule: By default, you are using the value below. If the characters at i and j match,
        # then you also use the value at the bottom right
        for row in range(len(s)-1,-1,-1):
            dp[row][len(t)] = 1
            for col in range(len(t)-1,-1,-1):
                dp[row][col] = dp[row+1][col]
                if s[row] == t[col]:
                    dp[row][col]+= dp[row+1][col+1]
        print(dp)
        return dp[0][0]
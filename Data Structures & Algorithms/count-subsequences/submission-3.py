

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0]*(len(t)+1)  #[s]
        dp[len(t)] = 1 # only 1 way to make string "" using "" (absolute base case)
        # Table rule: By default, you are using the value below. If the characters at i and j match,
        # then you also use the value at the bottom right
        # Optimal solution comes from the fact you're never using top rows

        for row in range(len(s)-1,-1,-1):
            newRow = [0]*(len(t)+1)
            newRow[len(t)]=1
            for col in range(len(t)-1,-1,-1):
                newRow[col] = dp[col]
                if s[row] == t[col]:
                    newRow[col]+= dp[col+1]
            dp=newRow
        print(dp)
        return dp[0]
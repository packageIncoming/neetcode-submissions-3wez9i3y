class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        R,C = len(text1),len(text2)
        dp= [[0]*(C+1) for i in range(R+1)]

        for r in range(1,R+1):
            for c in range(1,C+1):
                if text1[r-1] == text2[c-1]:
                    dp[r][c] = dp[r-1][c-1]+1
                else:
                    dp[r][c] = max(dp[r-1][c],dp[r][c-1])

        return dp[R][C]
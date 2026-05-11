class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        R,C = len(text1),len(text2)
        dp= [0]*(C+1) #for i in range(R+1)

        for r in range(1,R+1):
            prevRow = dp[0]
            for c in range(1,C+1):
                temp = dp[c] 
                if text1[r-1] == text2[c-1]:
                    dp[c] = prevRow+1
                else:
                    dp[c] = max(dp[c],dp[c-1])
                prevRow=temp
                


        return dp[C]
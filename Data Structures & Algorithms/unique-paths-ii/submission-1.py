class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # i want to try solving this with bottom up DP
        # 2-row DP (bottom and right needed)
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        dp= [0] * COLS
        dp[-1] = 1 # needed for base case
        for r in range(ROWS-1,-1,-1):
            newRow = [0] * COLS
            for c in range(COLS-1,-1,-1):
                if obstacleGrid[r][c] != 1:
                    # no obstacle so can pass in value
                    newRow[c] = dp[c]
                    if (c+1) < COLS:
                        newRow[c] += newRow[c+1]
            dp=newRow
        return dp[0]
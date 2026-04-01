class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #DP
        ROWS=len(grid)
        COLS=len(grid[0])
        dp=[0]*COLS
        dp[-1] = grid[ROWS-1][COLS-1]

        #initialize bottom row, can only move right towards the end :
        for i in range(COLS-2,-1,-1):
            dp[i] = dp[i+1] + grid[ROWS-1][i]
        for r in range(ROWS-2,-1,-1):
            newRow = [0]*COLS
            for c in range(COLS-1,-1,-1):
                # by default value is what's below:
                newRow[c] = dp[c]
                if c < COLS-1:
                    newRow[c] = min(newRow[c],newRow[c+1])
                # then add what the value is at that cell
                newRow[c] += grid[r][c]
            dp=newRow
        return dp[0]
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid), len(grid[0])
        seen = set()
        def dfs(r,c):
            if (r,c) in seen: return 0
            if r >= ROWS or r <0 or c >= COLS or c < 0:
                return 1 # invalid so not land
            if grid[r][c] != 1:
                return 1 # not land
            # get all the perimeter
            seen.add((r,c))
            return dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
    
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return dfs(i,j) # find first land

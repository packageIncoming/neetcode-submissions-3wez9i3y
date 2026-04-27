'''
there is probably some sort of DSU solution

problem: count and return the number of islands
signal: number of connected componetns within a 2D graph

approach:
1.  Iterate over each node and run a DFS check
2. for each node that is a 1 increment islandCount
3. run a DFS algo starting from that node that converts every connected 1 to a 0


'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])
        DIRS = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(r,c):
            if r < 0 or c < 0 or r >= R or c >= C: return
            if grid[r][c] == '1':
                grid[r][c] = '0'
                for dX,dY in DIRS:
                    dfs(r+dY,c+dX)

        res=0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    res+=1
                    dfs(r,c)
        return res
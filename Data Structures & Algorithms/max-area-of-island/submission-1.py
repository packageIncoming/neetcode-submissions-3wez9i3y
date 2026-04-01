class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        highestArea = 0

        y_bound = len(grid)
        x_bound = len(grid[0])

        def exploreStartingFrom(x,y):
            if x >= x_bound or y>= y_bound or x < 0 or y < 0:
                return 0 # bound check
            if grid[y][x] == 0:
                return 0
            # atp the cell is in-bounds and is a 1
            grid[y][x] = 0 # flip so it's not counted again
            return 1 + exploreStartingFrom(x+1,y) + exploreStartingFrom(x-1,y) + exploreStartingFrom(x,y+1) + exploreStartingFrom(x,y-1)

        for y in range(y_bound):
            for x in range(x_bound):
                if grid[y][x] == 1:
                    highestArea = max(highestArea, exploreStartingFrom(x,y))

        return highestArea

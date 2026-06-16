class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        highestArea = 0

        self.running_tot=0
        self.max = 0

        y_bound = len(grid)
        x_bound = len(grid[0])

        def exploreStartingFrom(x,y):
            if x >= x_bound or y>= y_bound or x < 0 or y < 0:
                return 0 # bound check
            if grid[y][x] == 0:
                return

            grid[y][x] = 0
            self.running_tot+=1
            exploreStartingFrom(x+1,y)
            exploreStartingFrom(x-1,y)
            exploreStartingFrom(x,y+1)
            exploreStartingFrom(x,y-1)

            

        for y in range(y_bound):
            for x in range(x_bound):
                if grid[y][x] == 1:
                    self.running_tot=0
                    exploreStartingFrom(x,y)
                    self.max = max(self.max,self.running_tot)

        return self.max

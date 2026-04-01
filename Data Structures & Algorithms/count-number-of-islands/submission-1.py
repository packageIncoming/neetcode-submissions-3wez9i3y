class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        seenCells = set()

        y_bound = len(grid)
        x_bound = len(grid[0])

        def exploreStartingFrom(x,y,seenOnThisPath):
            if (x,y) in seenOnThisPath or x < 0 or y < 0 or x >= x_bound or y >= y_bound:
                return
            if grid[y][x] == '0': return
            # atp this is a valid, in-bound tile that is an island tile
            seenOnThisPath.add((x,y))
            seenCells.add((x,y))
            exploreStartingFrom(x+1,y,seenOnThisPath)
            exploreStartingFrom(x-1,y,seenOnThisPath)
            exploreStartingFrom(x,y+1,seenOnThisPath)
            exploreStartingFrom(x,y-1,seenOnThisPath)
            
            

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == '1' and (x,y) not in seenCells:
                    # this is a valid land spot, try exploring it
                    count+=1
                    exploreStartingFrom(x,y,set())
        return count

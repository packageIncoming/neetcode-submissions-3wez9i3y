class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        treasureQueue = []
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 0:
                    treasureQueue.append((x,y))
        
        # bfs on treasureQueue
        level = 0
        y_bound = len(grid)
        x_bound = len(grid[0])
        seen = set()
        DIRECTIONS = [[0,1],[0,-1],[1,0],[-1,0]]
        while len(treasureQueue) > 0:
            newQueue = []
            for coord in treasureQueue:
                if coord in seen: continue
                seen.add(coord)
                grid[coord[1]][coord[0]] =level
                for direction in DIRECTIONS:
                    newX,newY = coord[0]+direction[0], coord[1] + direction[1]
                    if newX < x_bound and newX >= 0 and newY < y_bound and newY >= 0:
                        if (newX,newY) not in seen and grid[newY][newX] > 0:
                            newQueue.append((newX,newY))   
            level+=1
            treasureQueue = newQueue
            

            

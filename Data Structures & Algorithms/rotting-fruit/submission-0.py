class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi-source bfs just the same as 'walls and gates' problem, but 
        # return the level variable at the end, also track a 'freshCount' and 
        # decrement whenever a fresh is converted to rotted; if freshCount DNE 0 then return -1 else level
        rotQueue = collections.deque()
        y_bound = len(grid)
        x_bound = len(grid[0])
        seen = set()
        level=0
        freshCount = 0

        for y in range(y_bound):
            for x in range(x_bound):
                if grid[y][x] == 2:
                    rotQueue.append((x,y))
                if grid[y][x] == 1:
                    freshCount+=1
        
        while rotQueue:
            for i in range(len(rotQueue)):
                coords = rotQueue.popleft()
                if coords in seen: continue
                if coords[0] >= x_bound or coords[0] < 0 or coords[1] >= y_bound or coords[1] < 0: continue
                seen.add(coords)
                if grid[coords[1]][coords[0]] == 1:
                    # fresh, rot it (decrement freshCount) and add its neighbors
                    freshCount -=1
                    grid[coords[1]][coords[0]] = 2

                if grid[coords[1]][coords[0]] == 2:
                    # rotted, so add its neighbors
                    rotQueue.append((coords[0]+1,coords[1]))
                    rotQueue.append((coords[0]-1,coords[1]))
                    rotQueue.append((coords[0],coords[1]+1))
                    rotQueue.append((coords[0],coords[1]-1))
            if freshCount  == 0: break
            level+=1


        
        if freshCount == 0:
            return level
        else:
            return -1
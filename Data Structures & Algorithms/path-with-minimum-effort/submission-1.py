'''
-   Graph problem, goal is to minimize effort
    - Effort is defined as MAXIMUM abs difference between two consecutive cells, abs(cur-nxt)
-   Somehow keep track of current lowest
-   Valid directions are UP, DOWN, LEFT, RIGHT
-       DIFFERENT from other Bottom up DP problems where you only move right or down
-       complicates the bottom-up solution

What solutions stick out to me?:
1. Dijkstra's algorithm
2. Bottom-up dynamic programming

Actually, I think #2 wouldn't work since it applies better(?) when movement is limited (i.e. only right or down)

It would be easier to do #1 


'''


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        GOAL_R = rows-1
        GOAL_C = cols-1

        DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1)]


        heap = []   # items added as (cost,row,col)

        heapq.heappush(heap,(0,0,0))

        def validCell(row,col):
            if row >= rows or row < 0 or col >= cols or col < 0:
                return False
            else:
                return True

        min_efforts = [[float('inf') for i in range(cols)] for j in range(rows)]

        while heap:
            cost,row,col = heapq.heappop(heap)
            if row == GOAL_R and col == GOAL_C:
                # top element will be most efficient so return cost
                return cost
            if not validCell(row,col):
                continue


            # explore neighbors 
            for rX,cX in DIRECTIONS:
                # make sure it's a valid cell
                nR,nC = row+rX, col+cX
                if not validCell(nR,nC):
                    continue
                # add to the heap
                newCost=max(cost,abs(heights[nR][nC]-heights[row][col]))
                if newCost >= min_efforts[nR][nC]:
                    continue
                item = (newCost,nR,nC)
                heapq.heappush(heap,item)
                min_efforts[nR][nC] = newCost
        
        return -1

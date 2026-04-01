class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # adjacency from top, bottom, left right nodes
        ROWS, COLS = len(grid), len(grid[0])

        def safeGet(r,c):
            if r >=0 and c>=0 and r < ROWS and c < COLS:
                return grid[r][c]
            else:
                return -1
        def getAdj(r,c): # returns adjacent cells as arrays [[val,row,col]]
            DIRECTIONS = [[0,1],[0,-1],[1,0],[-1,0]]
            adjList = []
            for dR,dC in DIRECTIONS:
                val = safeGet(r+dR,c+dC)
                if val != -1:
                    adjList.append([val,r+dR,c+dC])
            return adjList
        
        minHeap = [(grid[0][0],0,0)] # objects of [val,row,col]
        minimumLevel = 0
        visited = {}
        i=0
        while minHeap:
            val,r,c = heapq.heappop(minHeap)
            #print(r,c)
            if (r,c) in visited:
                continue# don't revisit
            minimumLevel = max(minimumLevel,val)
            i+=1
            if r == ROWS-1 and c == COLS-1:
                #print(i)
                return minimumLevel
            visited[(r,c)] = val
            adj = getAdj(r,c)
            for adjVal,adjR,adjC in adj:
                if (adjR,adjC) not in visited:
                    heapq.heappush(minHeap,(max(adjVal,val),adjR,adjC))


        return minimumLevel
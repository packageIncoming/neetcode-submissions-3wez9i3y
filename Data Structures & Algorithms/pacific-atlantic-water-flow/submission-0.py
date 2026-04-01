

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pacificCells = set()
        atlanticCells = set()


        def checkReach(cell,seen,previousValue):
            if cell in seen or cell[0] >= ROWS or cell[1] >= COLS or cell[0] <0 or cell[1] < 0 or heights[cell[0]][cell[1]] < previousValue:
                return
            seen.add(cell)
            cellValue = heights[cell[0]][cell[1]]
            checkReach((cell[0]+1,cell[1]),seen,cellValue)
            checkReach((cell[0]-1,cell[1]),seen,cellValue)
            checkReach((cell[0],cell[1]+1),seen,cellValue)
            checkReach((cell[0],cell[1]-1),seen,cellValue)

        # get all the cells that can reach the pacific and atlantic (left and right)
        for i in range(ROWS):
            checkReach((i,0),pacificCells,float('-inf'))
            checkReach((i,COLS-1),atlanticCells,float('-inf'))
        # get all the cells that can reach the pacific and atlantic (top  and bottom)
        for i in range(COLS):
            checkReach((0,i),pacificCells,float('-inf'))
            checkReach((ROWS-1,i),atlanticCells,float('-inf'))
        # return the overlap in the sets
        result = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacificCells and (r,c) in atlanticCells:
                    result.append([r,c])
        return result
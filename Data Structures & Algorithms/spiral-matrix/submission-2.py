class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS,COLS = len(matrix),len(matrix[0])
        TOP,BOTTOM = 0,ROWS
        LEFT,RIGHT = 0,COLS
        res=[]
        while TOP<BOTTOM and LEFT<RIGHT:
            #top row
            for c in range(LEFT,RIGHT):
                res.append(matrix[TOP][c])
            TOP+=1
            
            #right col
            #print(res)
            for r in range(TOP,BOTTOM):
                res.append(matrix[r][RIGHT-1])
            RIGHT-=1
            if not (LEFT < RIGHT and TOP < BOTTOM):
                break
            #bottom row
            #print(res)

            for c in range(RIGHT-1,LEFT-1,-1):
                res.append(matrix[BOTTOM-1][c])
            # left col
            BOTTOM-=1
            
            #print(res)

            for r in range(BOTTOM-1,TOP-1,-1):
                res.append(matrix[r][LEFT])

            LEFT+=1
           # print(res)


        return res
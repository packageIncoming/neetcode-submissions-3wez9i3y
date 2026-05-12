class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        m,n = len(matrix),len(matrix[0])

        TOP,BOTTOM,LEFT,RIGHT = 0,m,0,n

        while TOP<BOTTOM and LEFT<RIGHT:
            for i in range(LEFT,RIGHT):
                res.append(matrix[TOP][i])
                print(res[-1])
            TOP+=1

            for i in range(TOP,BOTTOM):
                res.append(matrix[i][RIGHT-1])
            RIGHT-=1

            if not (TOP<BOTTOM) or not (LEFT<RIGHT):
                break

            for i in range(RIGHT-1,LEFT-1,-1):
                res.append(matrix[BOTTOM-1][i])
            BOTTOM-=1


            for i in range(BOTTOM-1,TOP-1,-1):
                res.append(matrix[i][LEFT])
                print(res[-1])
            LEFT+=1

        return res
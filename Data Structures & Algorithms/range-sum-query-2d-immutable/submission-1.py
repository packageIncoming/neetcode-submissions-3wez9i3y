'''
every cell id the area sum where that cell is the bottom right corner
and the top left is 0,0

so if you're given two points (r1,c1) which is TL and (r2,c2) which is BR
then the sum over that region is

self.matrix[r2][c2] - self.matrix[r2][c1-1] - self.matrix[r1-1][c2] + self.matrix[r1-1][c1-1]
'''


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = []

        R,C = len(matrix),len(matrix[0])

        for r in range(R):
            row=[]
            for c in range(C):
                topRect = self.matrix[r-1][c] if r-1>-1 else 0
                leftRect = row[c-1] if c-1>-1 else 0
                overlap = self.matrix[r-1][c-1] if (c-1>-1 and r-1>-1) else 0
                row.append(topRect+leftRect-overlap + matrix[r][c])
            self.matrix.append(row)
    def get(self,r,c):
        if r<0 or c<0 or r >= len(self.matrix) or c >= len(self.matrix[0]):
            return 0
        else:
            return self.matrix[r][c]


        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r2,c2 = row2,col2
        r1,c1 = row1,col1
        return self.get(r2,c2) - self.get(r2,c1-1) - self.get(r1-1,c2) + self.get(r1-1,c1-1)



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
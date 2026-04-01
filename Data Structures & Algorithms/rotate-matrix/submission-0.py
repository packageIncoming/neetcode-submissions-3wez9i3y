class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # rotation: rows from top to bottom become columns from right to left
        N=len(matrix)
        # 1. reverse rows vertically
        for i in range(N//2):
            temp = matrix[N-1-i]
            matrix[N-1-i] = matrix[i]
            matrix[i] = temp
        #print(matrix)
        # 2. transpose matrix (rows-> cols)
        # if you go diagonally then you can just reverse cells positions (mirroring)
        for i in range(N):
            for j in range(i,N):
                rowVal = matrix[i][j]
                colVal = matrix[j][i]
                matrix[i][j] = colVal
                matrix[j][i] = rowVal
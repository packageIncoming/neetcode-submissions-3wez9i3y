class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M = len(matrix)
        N = len(matrix[0])
        # get all cells where there is a 0 and mark the top row and left col cell as 0 in that row/col
        # then iterate over matrix again, turning cells to 0s if their top row or left col is a 0
        rowZero = False
        for r in range(M):
            for c in range(N):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0:
                        matrix[r][0] = 0
                    else:
                        rowZero  = True
        for r in range(1,M):
            for c in range(1,N):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if matrix[0][0] == 0:
            for r in range(M):
                matrix[r][0] = 0
        if rowZero:
            for c in range(N):
                matrix[0][c] =0





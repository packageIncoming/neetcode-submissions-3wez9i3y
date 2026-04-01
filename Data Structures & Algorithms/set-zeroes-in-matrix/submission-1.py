class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        M = len(matrix)
        N = len(matrix[0])
        rows=set()
        cols=set()
        # get all cells where there is a 0
        # then iterate over matrix again, turning cells to 0s if their row is in rows or their col is in cols
        for r in range(M):
            for c in range(N):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)
        for r in range(M):
            for c in range(N):
                if r in rows or c in cols:
                    matrix[r][c]=0

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        newMatrix = [[0]* ROWS for i in range(COLS)] # cols,rows
        for r in range(ROWS):
            for c in range(COLS):
                newMatrix[c][r] = matrix[r][c]
        return newMatrix
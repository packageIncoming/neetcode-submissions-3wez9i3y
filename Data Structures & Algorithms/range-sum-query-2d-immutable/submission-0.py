class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS,COLS = len(matrix),len(matrix[0])
        self.computedMatrix =[[0] * (COLS+1) for r in range(ROWS+1)]
        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.computedMatrix[r][c+1]
                self.computedMatrix[r+1][c+1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # 4 areas: the overlap square, the top, the left, and the raw square (from r2,c2)
        row1,col1 = row1+1, col1+1
        row2,col2 = row2+1,col2+1 # increment to align with self.computedMatrix
        rawArea = self.computedMatrix[row2][col2]
        topArea = self.computedMatrix[row1-1][col2]
        leftArea = self.computedMatrix[row2][col1-1]
        overlapArea = self.computedMatrix[row1-1][col1-1]
        return rawArea - (topArea + leftArea - overlapArea)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

'''Ideas:
    It looks like the original matrix is not accessed nor used at all after the matrix has been initialized
    Meaning we could get away with only storing the sums

    The stored matrix, self.matrix, would have cells matrix[r][c] that represent the sum of elements up to
    and including that cell


'''
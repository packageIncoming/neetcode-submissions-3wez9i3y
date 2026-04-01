class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        topRow=[0]*n
        topRow[n-1] = 1
        bottomRow=[0]*n
        for i in range(m):
            for cell in range(n-1,-1,-1):
                rightCell = 0
                if cell+1<n:
                    rightCell = topRow[cell+1]
                bottomCell = bottomRow[cell]
                topRow[cell] = max(bottomCell+rightCell,1)
            bottomRow = topRow
            topRow = [0]*n
        return bottomRow[0]
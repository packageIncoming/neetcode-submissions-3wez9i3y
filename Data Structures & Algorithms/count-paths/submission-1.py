class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prevRow = [1]*n
        curRow = [0]*n

        for i in range(m-1):
            for c in range(n-1,-1,-1):
                curRow[c] = prevRow[c] # can always move down
                if (c+1)<n:
                    curRow[c] += curRow[c+1] # can now also move right
            prevRow = curRow
            curRow = [0]*n
        return prevRow[0]
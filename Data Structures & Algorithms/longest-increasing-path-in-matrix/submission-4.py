class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        r,c = len(matrix),len(matrix[0])
        memo = [[-1]* c for _ in range(r)]
        def validCell(row,col):
            if row >= r or col >= c or row < 0 or col < 0:
                return False
            return True
        

        def getLongestPathStartingAt(row,col,seen,lastValue):
            if (row,col) in seen or  validCell(row,col) is False:
                return 0
            # now we know it's valid and unseen
            #print(row,col)
            if lastValue and lastValue >= matrix[row][col]:
                return 0 # not increasing
            if memo[row][col]!=-1:
                return memo[row][col]
            # add to seen
            seen.add((row,col))
            # explore cardinal coords
            DIRECTIONS = [[0,1],[0,-1],[1,0],[-1,0]]
            length = 1
            for x,y in DIRECTIONS:
                newRow,newCol = row+x, col+y
                if validCell(newRow,newCol):
                    length = max(length,1+getLongestPathStartingAt(newRow,newCol,seen,matrix[row][col]))
                    if (newRow,newCol) in seen:
                        seen.remove((newRow,newCol))
            memo[row][col] = length
            return length

        longestPath = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                length = getLongestPathStartingAt(i,j,set(),None)
                longestPath = max(longestPath,length)
        return longestPath
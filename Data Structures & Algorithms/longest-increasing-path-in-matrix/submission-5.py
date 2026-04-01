class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        r,c = len(matrix),len(matrix[0])
        memo = {}
        DIRECTIONS = [[0,1],[0,-1],[1,0],[-1,0]]

        def validCell(row,col):
            if row >= r or col >= c or row < 0 or col < 0:
                return False
            return True
        

        def getLongestPathStartingAt(row,col,lastValue):
            tag = (row,col)
            if  validCell(row,col) is False:
                return 0
            # now we know it's valid and unseen
            #print(row,col)
            if lastValue >= matrix[row][col]:
                return 0 # not increasing
            if tag in memo:
                return memo[tag]

            # explore cardinal coords
            length = 1
            for x,y in DIRECTIONS:
                newRow,newCol = row+x, col+y
                if validCell(newRow,newCol):
                    length = max(length,1+getLongestPathStartingAt(newRow,newCol,matrix[row][col]))
            memo[tag] = length
            return length

        longestPath = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                length = getLongestPathStartingAt(i,j,-1)
                longestPath = max(longestPath,length)
        return longestPath
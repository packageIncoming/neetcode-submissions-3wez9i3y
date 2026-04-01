'''
The n-queens puzzle is the problem of 
placing n queens on an n x n chessboard so that no two queens can attack each other.

A queen in a chessboard can attack horizontally, vertically, and diagonally.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a unique board layout where the queen pieces are placed. 
'Q' indicates a queen and '.' indicates an empty space.

You may return the answer in any order.

Observations:
- Starting from the top row and going downwards
- Given n queens and an nxn chessboard there are n^n possible combinations
- Perhaps a brute force solution would be to generate all possible combinations (highly inefficient)
- No two queens can be present on the same row and column
'''

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []

        baseBoard = ['.'*n for i in range(n)]

        def validSolution(solution): # solution is a hashset of queen positions (x,y)
            if len(solution) == 0: return False
            for queen in solution:
                # since we are moving from top to bottom we don't need to check rows
                # but we need to check columns and diagonals
                # 1, check if this queen position shares the same column
                for y in range(queen[1]): # check from top to queen's y
                    if (queen[0],y) in solution:
                        return False # solution already exists
                for y in range(queen[1]+1,n): # check from queen y to bottom of board
                    if (queen[0],y) in solution:
                        return False # solution already exists
                # 2, check diagonals
                # 2a, check bottom right diagonal
                row, col = queen[0]+1, queen[1]+1
                while row < n and col < n:
                    if (row,col) in solution: return False
                    row+=1
                    col+=1
                # 2b, check bottom left diagonal
                row, col = queen[0]-1, queen[1]+1
                while row >=0  and col < n:
                    if (row,col) in solution: return False
                    row-=1
                    col+=1
                # 2c, check top right diagonal
                row, col = queen[0]+1, queen[1]-1
                while row < n  and col >=0:
                    if (row,col) in solution: return False
                    row+=1
                    col-=1
                # 2d, check top left diagonal
                row, col = queen[0]-1, queen[1]-1
                while row >=0   and col >=0:
                    if (row,col) in solution: return False
                    row-=1
                    col-=1
            return True


        def solve(colNumber, curSolution):
            if colNumber >= n:
                solutions.append(curSolution.copy())
                return
            for i in range(n):
                curSolution.add((i,colNumber))
                #print(curSolution)
                #print(validSolution(curSolution))
                if validSolution(curSolution):
                    solve(colNumber+1,curSolution)
                curSolution.remove((i,colNumber))
        solve(0,set())
        boardSolutions = []
        for solution in solutions:
            board =[]
            for y in range(n):
                row = ""
                for x in range(n):
                    if (x,y) in solution:
                        row+='Q'
                    else:
                        row+='.'
                board.append(row)
            boardSolutions.append(board)
        return boardSolutions
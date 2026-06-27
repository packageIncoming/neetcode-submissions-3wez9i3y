'''
idea:
have a dict of sets by row,col,block

the tricky part is calculating what block (3x3 section) a given [r][c] cell belongs to




'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_sets=defaultdict(set)
        row_sets=defaultdict(set)
        block_sets=[[set() for i in range(3)] for j in range(3)]

        for r in range(9):
            for c in range(9):
                if board[r][c] in row_sets[r] or board[r][c] in col_sets[c]:
                    return False
                block = block_sets[r//3][c//3]
                if board[r][c] in block:
                    return False
                if board[r][c] != '.':
                    row_sets[r].add(board[r][c])
                    col_sets[c].add(board[r][c])
                    block.add(board[r][c])


        return True
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # get border o's, then any inner o's not on border that are connected are 'safe', otherwise flip
        ROWS = len(board)
        COLS=  len(board[0])
        borderO = set()
        safeO = set()
        for row in range(ROWS):
            if board[row][0] == 'O':
                borderO.add((row,0))
            if board[row][COLS-1] == 'O':
                borderO.add((row,COLS-1))
        for col in range(COLS):
            if board[0][col] == 'O':
                borderO.add((0,col))
            if board[ROWS-1][col] == 'O':
                borderO.add((ROWS-1,col))
        # dfs
        def getSafeCells(cell):
            if cell in safeO: return
            if cell[0] >=ROWS or cell[1] >= COLS or cell[0] < 0 or cell[1] < 0: return
            if board[cell[0]][cell[1]] != "O": return
            # in board, O value, unseen
            safeO.add(cell)
            getSafeCells((cell[0]+1,cell[1]))
            getSafeCells((cell[0]-1,cell[1]))
            getSafeCells((cell[0],cell[1]+1))
            getSafeCells((cell[0],cell[1]-1))

        for bO in borderO:
            getSafeCells(bO)
        for row in range(ROWS):
            for col in range(COLS):
                if (row,col) not in safeO and board[row][col] == 'O':
                    board[row][col] = 'X'
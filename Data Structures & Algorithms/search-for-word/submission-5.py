class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        Y = len(board)
        X = len(board[0])
        seen  =set()
        def dfs(letterIdx,x,y):

            if x >= X or x < 0 or y >=Y or y < 0:
                return False # OOB

            if board[y][x] != word[letterIdx]:
                return False
            if letterIdx == len(word)-1:
                return True

            DIRS = [[1,0],[-1,0],[0,1],[0,-1]]
            for dX,dY in DIRS:
                if (x+dX,y+dY) in seen: continue
                seen.add((x+dX,y+dY))
                if dfs(letterIdx+1,x+dX,y+dY):
                    return True
                seen.remove((x+dX,y+dY))
            return False

        # first find points from which you can start
        for y in range (len(board)):
            for x in range(len(board[0])):
                if board[y][x] == word[0]:
                    seen = set() # clear seen for new run
                    seen.add((x,y))
                    if dfs(0,x,y):
                        return True
        return False
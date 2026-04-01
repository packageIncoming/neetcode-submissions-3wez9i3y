class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        # get start points 
        # recursively look for solution starting from each startpoint
        rowBound = len(board)
        colBound = len(board[0]) # assuming all rows have the same # of elements

        def dfs(x,y,letterIdx,seenSet):
            if x >= rowBound or x <0:
                return False
            if y >= colBound or y < 0:
                return False

            if (x,y) not in seenSet and letterIdx < len(word) and board[x][y] == word[letterIdx]:
                seenSet.add((x,y))
                if letterIdx == len(word) -1 :
                        return True
                if dfs(x+1,y,letterIdx+1,seenSet):
                    return True
                if dfs(x-1,y,letterIdx+1,seenSet):
                    return True 
                if dfs(x,y+1,letterIdx+1,seenSet):
                    return True
                if dfs(x,y-1,letterIdx+1,seenSet):
                    return True
                seenSet.remove((x,y))
            else:
                return False
        for i in range(len(board)):
            row = board[i]
            for j in range(len(row)):
                if row[j] == word[0]:
                    # valid start
                    if dfs(i,j,0,set()) == True:
                        return True
        return False
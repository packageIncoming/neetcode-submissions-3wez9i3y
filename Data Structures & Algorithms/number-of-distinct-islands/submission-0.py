'''
Same structure as # islands
but the problem is in counting distinct islands by shape

problem becomes how do you capture the shape of an island?
    Or how do you make sure that you're not duplicating an island?

Islands are not guaranteed to be square so can't just capture dimensions

If you go top to bottom, left to right, the first cell you'll encounter is always 
the top left cell of an island

What determines if two islands are the same?
    If they have the same shape and are translations of each other
How exactly do you determine shape?
    This is a bit tough
How can you determine if they are translations of each other?
    If you start from the same cell and perform the exact same movements (up down left right)
    and they 'end' at the same time OR they differ at least once 

(USED HINT)

Reference each node WRT origin (top-left)


'''


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])

        curIslands = set() # set of tuples of tuples

        DIRS = [[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(origR,origC,dR,dC,curSeen):
            R,C = origR+dR,origC+dC
            if R<0 or C < 0 or R >= m or C >= n:
                return # OOB
            if grid[R][C] != 1:
                return # Invalid

            curSeen.append((dR,dC))
            grid[R][C] = 0 # prevent going back
            for dX,dY in DIRS:
                dfs(origR,origC,dR+dX,dC+dY,curSeen)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    cur = [] # set of tuples of coords
                    dfs(r,c,0,0,cur)
                    curIslands.add(tuple(cur))

        return len(curIslands)


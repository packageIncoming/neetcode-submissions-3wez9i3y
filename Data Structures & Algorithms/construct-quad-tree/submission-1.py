"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        n = len(grid)

        def dfs(r,c,n):

            allSame=True
            for i in range(n):
                for j in range(n):
                    if  grid[r + i][c + j] != grid[r][c]:
                        allSame = False
                        break
            if allSame == True:
                return Node(grid[r][c],True)
            else:
                node= Node(0,False)
                n= n//2
                node.topLeft = dfs(r,c,n)
                node.topRight = dfs(r,c+n,n)
                node.bottomLeft = dfs(r+n,c,n)
                node.bottomRight = dfs(r+n,c+n,n)
                return node            
        return dfs(0,0,n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def getGoodNodes(node,curMax):
            if node and node.val >= curMax:
                self.count+=1
                getGoodNodes(node.left,node.val)
                getGoodNodes(node.right,node.val)
            elif node and node.val < curMax:
                getGoodNodes(node.left,curMax)
                getGoodNodes(node.right,curMax)
        getGoodNodes(root,root.val)
        return self.count
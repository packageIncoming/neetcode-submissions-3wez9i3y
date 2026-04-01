# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res=0
        def getMaxHeight( node):
            if node is None:
                return 0
            left = getMaxHeight(node.left)
            right = getMaxHeight(node.right)
            self.res = max(self.res,left+right)
            return 1 + max(getMaxHeight(node.left),getMaxHeight(node.right))
        getMaxHeight(root)
        return self.res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recursiveDepth(self,root,d):
        if root is None:
            return d
        return max(self.recursiveDepth(root.left,d+1),self.recursiveDepth(root.right,d+1))
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recursiveDepth(root,0)
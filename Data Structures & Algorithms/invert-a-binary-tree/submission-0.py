# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recursiveInvert(self, node):
        if node is None:
            return
        else:
            node.left, node.right = node.right,node.left
            self.recursiveInvert(node.left)
            self.recursiveInvert(node.right)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.recursiveInvert(root)
        return root
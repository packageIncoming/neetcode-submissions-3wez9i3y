# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def helper(parent,node):
            if node:
                helper(node,node.left)
                helper(node,node.right)
                if node.val == target and node.left is None and node.right is None:
                    if node == parent.left:
                        parent.left = None
                    else:
                        parent.right = None
        
        helper(root,root.left)
        helper(root,root.right)
        if root.left is None and root.right is None and root.val is target:
            return None
        else:
            return root


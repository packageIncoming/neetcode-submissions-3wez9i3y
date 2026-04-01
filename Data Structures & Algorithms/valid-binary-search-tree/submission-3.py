# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkValid(node,lowBound,upBound):
            if not node:
                return True
            if node.val >= upBound or node.val <= lowBound:
                return False
            return True and checkValid(node.left,lowBound,node.val) and checkValid(node.right,node.val,upBound)
        return checkValid(root,float('-inf'),float('inf'))
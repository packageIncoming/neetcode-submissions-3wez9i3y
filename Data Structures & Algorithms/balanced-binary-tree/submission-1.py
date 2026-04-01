# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.result = True
        def heightCheck(node):
            if node is None:
                return 0
            left = heightCheck(node.left)
            right = heightCheck(node.right)
            #print(f"node {node.val} has left height {left} right height {right}")

            if (abs(left-right) > 1):
                self.result = False
            return 1 + max(left,right)
        heightCheck(root)
        return self.result
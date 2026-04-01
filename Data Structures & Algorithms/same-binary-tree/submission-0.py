# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.balanced=True
        def balanceCheck(pNode,qNode):
            if (not pNode and not qNode):
                return True
            if (not pNode and qNode) or (pNode and not qNode) or (pNode.val != qNode.val):
                self.balanced=False
                return False
            leftBalanced = balanceCheck(pNode.left,qNode.left)
            rightBalanced = balanceCheck(pNode.right,qNode.right)
            return leftBalanced and rightBalanced
        balanceCheck(p,q)
        return self.balanced
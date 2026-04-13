# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Goal: Validate a tree as a BST
Left mustbe less than parent
Right must be less than parent
Children must also be BSTs


First idea:
Keep track of the "working range", updating either the bottom or top if you move left
or right; start off (-inf,inf)

ex [2,1,3]
v(2,-inf,inf) VALID
    - move left v(1,-inf,2) VALID
    - move right v(3,2,inf) VALID

'''

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node,lBound,rBound):
            if node is None:
                return True
            if lBound < node.val < rBound:
                return validate(node.left,lBound,node.val) and validate(node.right,node.val,rBound)
            else:
                return False
        return validate(root,float('-inf'),float('inf'))
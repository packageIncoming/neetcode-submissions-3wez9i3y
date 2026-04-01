# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None: 
            node = TreeNode(val)
            return node
        def helper(curNode,valToInsert):
            if valToInsert > curNode.val:
                if not curNode.right:
                    node = TreeNode(valToInsert)
                    curNode.right=node
                else:
                    helper(curNode.right,valToInsert)
            elif valToInsert < curNode.val:
                if not curNode.left:
                    node = TreeNode(valToInsert)
                    curNode.left = node
                else:
                    helper(curNode.left,valToInsert)
        helper(root,val)
        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traveled = []
        def travel(node):
            if node is None:
                return
            travel(node.left)
            travel(node.right)
            traveled.append(node.val)        
        travel(root)        
        return traveled
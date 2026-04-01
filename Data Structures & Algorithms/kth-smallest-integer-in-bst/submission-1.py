# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.vals = []
            
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            self.vals.append(node.val)
            dfs(node.right)
        dfs(root)
        return self.vals[k-1]
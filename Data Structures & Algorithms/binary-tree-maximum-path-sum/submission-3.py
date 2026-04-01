# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float("-inf")
        def dfs(node):
            if node is None:
                return 0
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            max_with_split = left_max + right_max + node.val
            self.maxSum = max(self.maxSum,max_with_split)
            return max(0,left_max+node.val,right_max+node.val)
        dfs(root)
        return self.maxSum
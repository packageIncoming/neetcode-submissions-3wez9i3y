# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lvls = defaultdict(list)
        def dfs(node,i):
            if node is None:
                return
            lvls[i].append(node.val)
            dfs(node.left,i+1)
            dfs(node.right,i+1)
        dfs(root,0)
        return list(lvls.values())

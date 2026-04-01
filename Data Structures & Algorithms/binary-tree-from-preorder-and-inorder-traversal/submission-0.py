# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.hmap = {val:idx for idx, val in enumerate(inorder)}
        self.cur_idx = 0
        def dfs(l,r):
            if l > r: return
            root_val = preorder[self.cur_idx]
            self.cur_idx+=1
            mid = self.hmap[root_val]
            root = TreeNode(root_val)
            root.left = dfs(l,mid-1)
            root.right = dfs(mid+1,r)
            return root
        return dfs(0,len(preorder)-1)
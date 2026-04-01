# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.min = min(p.val,q.val)
        self.max = max(p.val,q.val)

        def findLCA(r,p,q):
            if  r.val >= self.min and r.val <= self.max:
                return r
            if r.val < self.min:
                return findLCA(r.right,p,q)
            else:
                return findLCA(r.left,p,q)
        return findLCA(root,p,q)
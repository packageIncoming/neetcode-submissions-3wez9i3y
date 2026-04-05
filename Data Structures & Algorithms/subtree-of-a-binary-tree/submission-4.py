# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
2 steps
1. find the subroot within root tree
2. start matching to make sure everything matches
'''

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def match(cur,nodeToMatch):
            if cur is None and nodeToMatch is None:
                return True # leaf
            if cur is None and nodeToMatch is not None:
                return False # leaf but shouldn't be
            if cur is not None and nodeToMatch is None:
                return False # expected null got leaf
            
            if cur.val == nodeToMatch.val:
                return match(cur.left,nodeToMatch.left) and match(cur.right,nodeToMatch.right)
            else:
                return False

        def dfs(node):
            if node is None:
                return False
            if node.val == subRoot.val:
                if match(node,subRoot):
                    return True
            return dfs(node.left) or dfs(node.right)
        return dfs(root)
        
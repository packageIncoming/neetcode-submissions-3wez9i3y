# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        lvls = []
        if root is None: return []
        q = deque()
        q.append(root)
        while q:
            l = []
            for i in range(len(q)):
                top = q.popleft()
                l.append(top.val)
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
            lvls.append(l)
        return lvls


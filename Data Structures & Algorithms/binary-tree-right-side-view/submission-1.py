# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        rightSide = []
        nodes = collections.deque()
        nodes.append(root)
        while nodes:
            l = len(nodes)
            rightmost = None
            for i in range(l):
                node = nodes.popleft()
                if node:
                    rightmost = node
                    nodes.append(node.left)
                    nodes.append(node.right)
            if rightmost:
                rightSide.append(rightmost.val)
        return rightSide
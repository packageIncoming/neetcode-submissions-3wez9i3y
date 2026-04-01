# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def getMaxHeight(self, node,d):
        if node is None:
            return d
        else:
            return max(self.getMaxHeight(node.left,d+1),self.getMaxHeight(node.right,d+1))
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        nodes = deque()
        nodes.append(root)
        diameter = 0
        while len(nodes) != 0:
            node = nodes.popleft()
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
            diameter = max(diameter, self.getMaxHeight(node.left,0) + self.getMaxHeight(node.right,0))
        return diameter
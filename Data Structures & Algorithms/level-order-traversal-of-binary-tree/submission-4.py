# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = deque()
        nodes.append(root)
        layers = []
        while nodes:
            lSize = len(nodes)
            layer = []
            for i in range(lSize):
                node = nodes.popleft()
                if node:
                    layer.append(node.val)
                    nodes.append(node.left)
                    nodes.append(node.right)
            if layer:
                layers.append(layer)
        return layers
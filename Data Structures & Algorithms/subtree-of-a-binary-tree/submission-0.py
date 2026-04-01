# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.possible_starts = []

        def findStarts(node,sRoot):
            if not node:
                return
            if node.val == sRoot.val:
                self.possible_starts.append(node)
            findStarts(node.left,sRoot)
            findStarts(node.right,sRoot)
        def checkEquals(node,subNode):
            if not node and not subNode:
                return True
            elif (not node and subNode) or (node and not subNode):
                return False
            elif (node.val != subNode.val):
                return False
            return True and checkEquals(node.left,subNode.left) and checkEquals(node.right,subNode.right)
        findStarts(root,subRoot)
        for node in self.possible_starts:
            if checkEquals(node,subRoot) is True:
                return True
        return False
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Two nodes are directly linked if they have a connection between them
This means that we can rob all leaf nodes which sets up a recursive case:
    If node.left is None and node.right is None: return node.val
    If a node is None return 0 (DNE)

If a node only has a right node:
    Return max(node.val+ recursive(node.right.left), node.val + recursive(node.right.right), recursive(node.right))


If a node only has a left node:
    Return max(node.val+ recursive(node.left.left), node.val + recursive(node.left.right), recursive(node.left))

If a node has both a left AND right node:
    Basically a combination of left and right

You're either choosing a node and skipping the next generation OR you're skipping a node and moving to the next generation
    Recursive base cases make it simpler and reduce the amount of exitsence checks

'''
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        def recurse(node,i):
            if node is None:
                return 0 
            if node.right is None and node.left is None:
                return node.val

            if i in memo:
                return memo[i]

            if node.right and node.left is None:
                memo[i]= max(
                    node.val + recurse(node.right.left,2*(2*i+1)) + recurse(node.right.right,2*(2*i+1)+1),
                    recurse(node.right,2*i+1)
                )
                return memo[i]
                
            if node.left and node.right is None:
                memo[i]= max(
                    node.val + recurse(node.left.left,2*(2*i)) + recurse(node.left.right,2*(2*i)+1),
                    recurse(node.left,2*i)
                )
                return memo[i]

            memo[i]= max(
                    node.val + recurse(node.left.left,2*(2*i)) + recurse(node.left.right,2*(2*i)+1)
                    + recurse(node.right.left,2*(2*i+1)) + recurse(node.right.right,2*(2*i+1)+1),
                    recurse(node.right,2*i+1) + recurse(node.left,2*i),
                    
                
            )
            return memo[i]


        return recurse(root,1)
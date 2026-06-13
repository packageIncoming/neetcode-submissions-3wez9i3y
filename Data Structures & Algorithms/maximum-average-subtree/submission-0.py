# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
GOAL: find maximum average value of a subtree

Average value of a tree is the sum of its values divided by # of nodes

DFS seems like the smartest option to me here
    + some sort of recursive rule for calculating the average

Idea: 
    Calculate average at a node
    Update a global value that holds the max average
    Propagate up (return) a tuple of (sum_including_node,num_nodes)
    Average value is calculated as 
        (sum_left + sum_right + cur_node_val) / (num_left+num_right+1)
    We don't have to choose which average to return if we just update
    a global value

    Return the global value

'''

class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.mav = 0

        def dfs(node):
            if node is None:
                return (0,0)
            l_sum,l_count = dfs(node.left)
            r_sum,r_count = dfs(node.right)
            self.mav = max(
                self.mav,
                (l_sum+r_sum+node.val) / (l_count+r_count+1)
            )
            return  ((l_sum+r_sum+node.val), (l_count+r_count+1))

        dfs(root)

        return self.mav

        
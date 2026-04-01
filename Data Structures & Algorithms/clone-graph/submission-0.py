"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.hmap = {}
        # create node if its not already in the hmap
        # create all its adjacent nodes
        # then iterate over the neighbors of the original node, lookup in hmap and set to new node's neighbor
        def deepCopyStartingFrom(node: Optional['Node']):
            if node and node.val not in self.hmap:
                newNode = Node()
                newNode.val = node.val
                self.hmap[node.val] = newNode
            #newNode = self.hmap[node.val]
                for neighbor in node.neighbors:
                    deepCopyStartingFrom(neighbor)
                    newNode.neighbors.append(self.hmap[neighbor.val])
                return newNode

        return deepCopyStartingFrom(node)
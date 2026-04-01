"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        nodePairs = []
        cur = head
        m = {}
        while cur:
            newNode = Node(cur.val)
            nodePairs.append([cur,newNode])
            m[cur] = len(nodePairs)-1
            cur = cur.next
        #print(m)
        for i, nodePair in enumerate(nodePairs):
            original = nodePair[0]
            new = nodePair[1]
            
            #set next val
            if (i+1) < len(nodePairs):
                new.next = nodePairs[i+1][1]

            if original.random is not None:
                original_random_idx = m[original.random]
                new.random = nodePairs[original_random_idx][1]
                #print(original_random_idx)
            else:
                new.random  =None

        return nodePairs[0][1]

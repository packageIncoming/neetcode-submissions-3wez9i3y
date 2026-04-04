'''
Goal: Check whether the given edges make up a valid tree

What constitutes a valid tree?
-No orphans
-No loops


If you perform a BFS search starting at any index (say n=0)
then you should not run into the same node twice
BUT you should run into each node exactly ONCE

How do you make sure you're not going back up (since the edges are undirected?)
Use sets as adjacency lists and remove once explored(?)

Keep track of what's seen with a seen{} set

1. Create adjacency lists
2. Starting at n=0 expand the adjacent nodes
add the nodes to the queue
If ever the current node is seen, return False
once done expanding return len(seen) = n
'''

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = [set() for i in range(n)]
        for f,t in edges:
            if f == t: return False # no self loops
            adjList[f].add(t)
            adjList[t].add(f)
        
        q = deque()
        q.append(0)
        seen  =set()

        while q:
            top = q.popleft()
            if top in seen: return False # already explored
            # add to seen
            seen.add(top)
            # add its neighbors
            for neighbor in adjList[top]:
                q.append(neighbor)
                adjList[neighbor].remove(top) # prevent going backwards


        return len(seen) == n
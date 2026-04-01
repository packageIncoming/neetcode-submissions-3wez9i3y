class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) # node count
        parents = [i for i in range(n+1)]

        rank = [1 for i in range(n+1)]

        def findParent(node):
            curParent = parents[node]
            while curParent != parents[curParent]:
                parents[curParent] = parents[parents[curParent]]
                curParent = parents[curParent]
            return curParent

        def union(node1,node2):
            p1,p2 = findParent(node1), findParent(node2)
            if p1 ==p2:
                return False # already joined, cycle detected
            # different parents, join  based on which has higher rank
            if rank[p1] > rank[p2]:
                parents[p2] = p1
                rank[p1] += rank[p2]
            else:
                parents[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1,n2):
                return [n1,n2]
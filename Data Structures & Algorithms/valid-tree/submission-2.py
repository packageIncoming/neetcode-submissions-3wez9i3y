class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # first construct connections
        nodeToConnections = [set() for i in range(n)] # i = node, arr[i] = adjacent
        for i in range(len(edges)):
            edge = edges[i]
            nodeToConnections[edge[0]].add(edge[1])
            nodeToConnections[edge[1]].add(edge[0])
        allSeen = set()

        def cycleCheck(node):
            if node in allSeen:
                return False # we already saw this node so there must be a cycle present
            # not seen so add to seen
            allSeen.add(node)
            # now explore the children
            for child in nodeToConnections[node]:
                childConnections = nodeToConnections[child]
                childConnections.remove(node)
                if cycleCheck(child) == False:
                    return False
            return True
        return cycleCheck(0) and len(allSeen) == n
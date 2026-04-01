class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # create adj list
        adjList = [set() for i in range(n)]
        for edge in edges:
            adjList[edge[0]].add(edge[1])
            adjList[edge[1]].add(edge[0])

        seen = set()
        components = 0
        # for every node:
        # check if it's already seen
        # if not, increment component count
        # then explore children by DFS
        # similar to 'graph valid tree' (removing connections after exploration)
        # return # components

        def explore(node):
            if node in seen:
                print(node)
                return # already explored
            seen.add(node) # mark as explored
            for child in adjList[node].copy():
                adjList[child].remove(node) # remove connection to parent
                explore(child) # explore the child 


        for node in range(n):
            if node not in seen:
                components+=1
                explore(node)

        return components
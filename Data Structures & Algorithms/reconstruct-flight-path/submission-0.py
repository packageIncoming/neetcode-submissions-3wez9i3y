class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # directed graph, can have loops (from <-> to)
        # unweighted  but must be lexicographically the smallest (str < str)
        adjList = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adjList[src].append(dst)


        path=[]

        def dfs(node):
            #postorder
            while adjList[node]:
                neighbor = adjList[node].pop()
                dfs(neighbor)
            path.append(node)
            
            
        dfs("JFK")
        return path[::-1]
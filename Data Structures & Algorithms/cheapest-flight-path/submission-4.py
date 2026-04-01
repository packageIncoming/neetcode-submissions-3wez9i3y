class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # bellman ford using a queue
        costs = [float('inf') for _ in range(n)]
        costs[src]=0

        adjList = [[] for _ in range(n)]
        for f,t,p in flights:
            adjList[f].append((t,p)) # edges = to,price pairs

        q = deque() # arrs of (cost,sourceNode,stops)
        q.append((0,src,0))
        while q:
            cost,source,stopsTaken = q.popleft()
            if stopsTaken > k: continue
            # expand its neighbors
            for neighbor,neighborCost in adjList[source]:
                newCost = neighborCost+cost
                if newCost < costs[neighbor]:
                    # expand since it is cheaper
                    costs[neighbor]=newCost
                    q.append((costs[neighbor],neighbor,stopsTaken+1))


        return costs[dst] if costs[dst] != float('inf') else -1
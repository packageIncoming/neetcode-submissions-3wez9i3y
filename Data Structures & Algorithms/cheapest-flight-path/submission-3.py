class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # graph with weighted directed edges [from,to,price]
        # no duplicate flights and no self-loops
        # when creating the minHeap, add another property to the edges, stopNumber, which will count
        # what the stop is for that edge
        # whenever an edge is popped simply increment its stopNumber by 1 and its neighbors will inherit that

        # construct adjacency list (0 to n-1)
        adjList = [[] for i in range(n)]
        for start,destination,price in flights:
            adjList[start].append((destination,price))
        # construct minHeap
        minHeap = [(0,0,src)] # minHeap objects are tuples (cost,stopNumber,node)
        visited = set()
        minCost = float('inf')
        while minHeap:
            cost,stopNumber,node = heapq.heappop(minHeap)
            if node == dst: # exit if we found the end
                minCost = min(minCost,cost)
                continue
            if stopNumber > k: continue # can't explore this path anymore OR already visited
            if node != dst:
                visited.add(node) # add to visited
                stopNumber+=1 # increment stop # for neighbors
                for edge in adjList[node]:
                    destination,price = edge[0],edge[1]
                    print(f"added {price+cost}, {stopNumber}, {destination}")
                    heapq.heappush(minHeap,(price+cost,stopNumber,destination)) # add to heap
            
        return minCost if minCost != float('inf') else -1

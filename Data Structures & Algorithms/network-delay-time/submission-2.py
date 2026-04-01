class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # create adjacency list
        adjList = defaultdict(list)
        # fill adj list with connections
        for src,target,time in times:
            adjList[src].append((time,target))
        minHeap = [(0,k)]
        visited = set()
        longestTime = 0
        # the shortest time for all n nodes to receive the signal would be the longest time in visited
        while minHeap:
            time,node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            longestTime = time
            
            for edgeTime,edgeNode in adjList[node]:
                if edgeNode not in visited:
                    heapq.heappush(minHeap,(time+edgeTime,edgeNode))

        if len(visited) != n: # means that not all nodes have been visited
            return -1
        else:
            return longestTime
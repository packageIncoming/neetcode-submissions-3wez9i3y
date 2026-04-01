class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # create adjacency list
        adjList = defaultdict(list)
        # fill adj list with connections
        for src,target,time in times:
            adjList[src].append((time,target))
        minHeap = [(0,k)]
        shortestTimes = {}
        longestTime = 0
        # the shortest time for all n nodes to receive the signal would be the longest time in shortestTimes
        while minHeap:
            time,node = heapq.heappop(minHeap)
            if node not in shortestTimes:
                shortestTimes[node] = time
                longestTime = max(longestTime,time)
            
            for edge in adjList[node]:
                edgeTime,edgeNode = edge[0],edge[1]
                if edgeNode not in shortestTimes:
                    heapq.heappush(minHeap,(time+edgeTime,edgeNode))

        if len(shortestTimes.keys()) != n: # means that not all nodes have been visited
            return -1
        else:
            return longestTime
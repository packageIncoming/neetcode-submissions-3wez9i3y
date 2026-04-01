class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def getDist(p1,p2):
            x1,y1=p1
            x2,y2=p2
            return abs(x1-x2) + abs(y1-y2)
        adjHash = defaultdict(list) # key = point, value = arr of edges where edges have [weight,point]
        for i in range(len(points)):
            # distance from i to j is the same as the distance from j to i, so no need to loop over all points over and over
            i_point = points[i]
            for j  in range(i+1,len(points)):
                
                j_point = points[j]
                dist = getDist(i_point,j_point)
                adjHash[i].append([dist,j])
                adjHash[j].append([dist,i])
        # now perform Prim's algorithm, constructing MST and getting the cost
        minHeap = [[0,0]] # value, point arrs
        mstCost=0
        visited = set()
        while len(visited) < len(points):
            dist,point = heapq.heappop(minHeap)
            if point in visited:
                continue # don't revisit
            mstCost+= dist
            visited.add(point)
            for neighborDist, neighborPoint  in adjHash[point]:
                if neighborPoint not in visited:
                    heapq.heappush(minHeap,[neighborDist,neighborPoint])

        return mstCost

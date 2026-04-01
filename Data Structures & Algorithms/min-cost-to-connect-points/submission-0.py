class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def getDist(p1,p2):
            x1,y1=p1
            x2,y2=p2
            return abs(x1-x2) + abs(y1-y2)
        adjHash = defaultdict(list) # key = point, value = arr of edges where edges have [weight,point]
        for i in range(len(points)):
            # distance from i to j is the same as the distance from j to i, so no need to loop over all points over and over
            for j  in range(i+1,len(points)):
                i_point = points[i]
                j_point = points[j]
                dist = getDist(i_point,j_point)
                adjHash[(i_point[0],i_point[1])].append([dist,tuple(j_point)])
                adjHash[(j_point[0],j_point[1])].append([dist,tuple(i_point)])
        # now perform Prim's algorithm, constructing MST and getting the cost
        #important note: selecting first point must choose the lowest value for it to make sense
        firstElem = [0,tuple(points[0])]
        for edge in adjHash[(points[0][0],points[0][1])]:
            firstElem[0] = min(firstElem[0],edge[0])
        minHeap = [firstElem] # value, point arrs
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

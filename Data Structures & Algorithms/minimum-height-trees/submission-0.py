class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # create adjacency map:
        adjMap = defaultdict(list)
        for n1,n2 in edges:
            adjMap[n1].append(n2)
            adjMap[n2].append(n1)

        # bfs + caching distances on find
        memo = {} # tuple:dist 
        maxHeights = {} # int(node #):int(max height for that tree)

        def bfsExplore(node):
            q = deque()
            q.append(node)
            seen = set()
            depth=0

            while q:
                for i in range(len(q)):
                    topNode = q.popleft()
                    if topNode in seen: continue # ignore 
                    seen.add(topNode)
                    for adj in adjMap[topNode]:
                        if adj in seen: continue #ignore
                        q.append(adj)
                depth+=1
            return depth

        minHeight = float('inf')

        for i in range(n):
            maxHeights[i] = bfsExplore(i)
            minHeight = min(minHeight,maxHeights[i])

        print(minHeight,maxHeights)
        
        minHeightRoots = []
        for i in range(n):
            if maxHeights[i] == minHeight:
                minHeightRoots.append(i)
        return minHeightRoots
        

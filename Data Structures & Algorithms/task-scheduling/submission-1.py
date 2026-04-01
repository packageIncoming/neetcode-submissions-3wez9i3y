class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        # get frequencies
        freqs = defaultdict(int)
        for task in tasks:
            freqs[task]+=1
        # turn into heap
        heap = list([-val for val in freqs.values()])
        heapq.heapify(heap)
        #create queue
        q =collections.deque()
        currentCycle = 0
        while len(heap)>0 or len(q)>0:
            if heap:
                top = heapq.heappop(heap)
                top+=1
                if top <0:
                    q.append([top,currentCycle+n])
            else:
                time = q[0][1] # fast forward instead of wasting steps
            # check if value at front of queue can be reinserted
            if q and q[0][1] <= currentCycle:
                val = q.popleft()[0]
                heapq.heappush(heap,val)
            currentCycle+=1
        return currentCycle


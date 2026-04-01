class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        q_zip = list(zip(queries,range(len(queries))))
        output = [0]*len(queries)
        q_zip.sort()
        minHeap = []
        intervals_idx=0
        for q,idx in q_zip:
            while intervals_idx < len(intervals):
                interval = intervals[intervals_idx]
                if interval[0] <= q:
                    # starts before q
                    heapq.heappush(minHeap,(interval[1]-interval[0]+1,interval[1]))
                else:
                    break # starts after q so invalid
                intervals_idx+=1
            while minHeap and minHeap[0][1] < q:
                # remove all the intervals that end before q
                heapq.heappop(minHeap)
            output[idx] = minHeap[0][0] if minHeap else -1
        return output
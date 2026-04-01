class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # brute force solution: iterate over all intervals and find shortest one for each query
        output = []
        for query in queries:
            last_size = float('inf')
            for i in range(len(intervals)):
                interval = intervals[i]
                if query >= interval[0] and query <= interval[1]:
                    if interval[1]-interval[0]+1 < last_size:
                        last_size = interval[1]-interval[0]+1
            if last_size == float('inf'):
                last_size=-1
            output.append(last_size)
        return output
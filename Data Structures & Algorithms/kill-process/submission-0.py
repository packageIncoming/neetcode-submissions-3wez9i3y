'''
The smart thing to do here I think is to make it into an adjacency graph,
BFS adding explored pids to 2 queues (1 for bfs 1 for res) then return res queue


'''
class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        adj = defaultdict(list)
        for i in range(len(pid)):
            parent = ppid[i]
            adj[parent].append(pid[i])
        
        queue = deque()
        queue.append(kill)
        res = []

        while queue:
            p = queue.popleft()
            res.append(p)
            for c in adj[p]:
                queue.append(c)


        return res

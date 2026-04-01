class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            minlen = min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return "" # invalid ordering
            # now check to see the first differing character
            for j in range(minlen):
                if w1[j] != w2[j]:
                    # differing character found
                    adj[w1[j]].add(w2[j])
                    break # no need to check rest
        
        # now iterate over the graphs made 
        # if there is a cycle then that means there is an invalid ordering return ""
        visited = {}
        res=[]
        def dfs(node):
            if node in visited:
                return visited[node]
            visited[node]=True
            for neighbor in adj[node]:
                if dfs(neighbor):
                    return True
            visited[node]=False # clear it 
            res.append(node)
        for node in adj:
            if dfs(node):
                return ""
        return "".join(res[::-1])



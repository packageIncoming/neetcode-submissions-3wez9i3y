class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # the logic is more intensive for this than the actual recursion
        m, n = len(s), len(p)
        cache = [[-1]* (m+1) for i in range(n+1)]
        def dfs(i,j):
            if j == n:
                return i == m
            match= False
            if i < len(s) and( s[i] == p[j] or p[j] == "."):
                match=True
            
            if cache[j][i] != -1:
                return cache[j][i]

            if (j+1) < len(p) and p[j+1] == "*":
                cache[j][i] = ( dfs(i,j+2) or (match and dfs(i+1,j)) )
                return cache[j][i]
            if match:
                cache[j][i] =  dfs(i+1,j+1)
                return cache[j][i]
            cache[j][i] = False
            return cache[j][i]


        return dfs(0,0)

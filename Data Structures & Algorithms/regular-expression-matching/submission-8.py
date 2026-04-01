class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # the logic is more intensive for this than the actual recursion
        m, n = len(s), len(p)
        def dfs(i,j):
            if j == n:
                return i == m
            match= False
            if i < len(s) and( s[i] == p[j] or p[j] == "."):
                match=True

            if (j+1) < len(p) and p[j+1] == "*":
                return ( dfs(i,j+2) or (match and dfs(i+1,j)) )
            if match:
                return dfs(i+1,j+1)
            return False


        return dfs(0,0)

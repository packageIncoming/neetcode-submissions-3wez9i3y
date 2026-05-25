class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hmap = {}
        def dfs(i):
            if i >= len(s):
                return True
            if i in hmap:
                return hmap[i]
            hmap[i]=False
            for word in wordDict:
                if len(word)+i <= len(s) and s[i:i+len(word)] == word:
                    if dfs(i+len(word))==True:
                        hmap[i]=True
                        break
            return hmap[i]
        

        return dfs(0)
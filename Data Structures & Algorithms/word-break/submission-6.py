from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # create permutations of wordDict words with backtracking 
        # base case where len(curWord) == len(s), check if equal, if yes then return True
        # base case where len(curWord) > len(s), do nothing (invalid leaf)
        memo = {len(s):True}
        def dfs(i):
            nonlocal memo
            if i in memo:
                return memo[i]

            elif i > len(s):
                memo[i]= False
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    # this chunk matches, see if the rest matches
                    if dfs(i+len(word)):
                        memo[i] =  True
                        return True
            memo[i] =False
            return memo.get(i,False)
        return dfs(0)

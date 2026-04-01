class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # idea: piece together from dictionary 
        memo = {}

        def solve(i):
            if i == len(s):
                return 0
            if i > len(s):
                return float('inf')
            if i in memo:
                return memo[i]
            res= 1+solve(i+1)
            found=False
            for word in dictionary:
                r=len(word)+i
                if r > len(s): continue 
                subSection = s[i:r]
                if subSection == word:
                    res=  min(res,solve(r))
                    found=True
            memo[i]= res
            return memo[i]
        
        return solve(0)
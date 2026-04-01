'''
Insights and Intuitions:
At any two indices, two characters can either match or not match
- if they are a match then do nothing (no changes need to be made)
- if they are not a match then you can do one of the following
    - insert the required character
    - delete the unwanted character
    - replace the unwanted character with the wanted character
- How do you decide which of the three decisions to take?


'''


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[-1]*(len(word2)+1) for _ in range(len(word1)+1)] # [word1][word2]
        def dfs(idx1,idx2):
            if idx2 == len(word2) and idx1 == len(word1):
                return 0 # successfully made the word without letters remaining
            if idx2 == len(word2) and idx1 < len(word1):
                # we made the word but we have (len1-idx1) letters to remove
                return len(word1)-idx1
            if idx1 == len(word1) and idx2 < len(word2):
                # we ran out of letters in this path and we have (len2-idx2) letters to add
                 return len(word2)-idx2
            if cache[idx1][idx2] != -1:
                return cache[idx1][idx2]
                    
            if word1[idx1] == word2[idx2]:
                cache[idx1][idx2]= dfs(idx1+1,idx2+1) # we have a match, no need to do anything
            else:
                cache[idx1][idx2]= 1+ min(dfs(idx1,idx2+1),dfs(idx1+1,idx2),dfs(idx1+1,idx2+1))
            return cache[idx1][idx2]
        return dfs(0,0)
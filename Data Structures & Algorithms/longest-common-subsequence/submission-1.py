class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1]*len(text2) for i in range(len(text1))]  #memo[ptr1][ptr2]
        def findLCS(ptr1,ptr2):
            if ptr1 >= len(text1) or ptr2 >= len(text2):
                return 0 # OOB base case
            if memo[ptr1][ptr2]!=-1:
                return memo[ptr1][ptr2]
            if text1[ptr1] == text2[ptr2]:
                memo[ptr1][ptr2]= 1 + findLCS(ptr1+1,ptr2+1)
                return memo[ptr1][ptr2]
            else:
                memo[ptr1][ptr2]= max(findLCS(ptr1,ptr2+1),findLCS(ptr1+1,ptr2))
                return memo[ptr1][ptr2]
        return findLCS(0,0)
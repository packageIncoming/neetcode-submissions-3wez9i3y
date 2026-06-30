class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=[]

        w1p,w2p=0,0
        while w1p<len(word1) or w2p<len(word2):
            if w1p<len(word1):
                res+=word1[w1p]
                w1p+=1
            if w2p<len(word2):
                res+=word2[w2p]
                w2p+=1


        return ''.join(res)
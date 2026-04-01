class Solution:

    def partition(self, s: str) -> List[List[str]]:
        parts = []

        def isPalindrome(l,r):
            while l <=r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        curPart = []
        def createParts(i):
            if i >= len(s):
                parts.append(curPart.copy())
                return
            for j in range(i,len(s)):
                if isPalindrome(i,j):
                    curPart.append(s[i:j+1])
                    createParts(j+1)
                    curPart.pop()
        createParts(0)


        return parts



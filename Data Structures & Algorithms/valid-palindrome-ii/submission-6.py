class Solution:
    def validPalindrome(self, s: str) -> bool:

        def helper(l,r,c):
            while l <r:
                if s[l]!=s[r]:
                    if c==True:
                        return False
                    else:
                        if helper(l+1,r,True):
                            return True
                        elif helper(l,r-1,True):
                            return True
                        return False
                l+=1
                r-=1
            return True
        
        return helper(0,len(s)-1,False)
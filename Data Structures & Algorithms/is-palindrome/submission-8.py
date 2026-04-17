class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1



        while l <=r:
            while l<len(s) and (not s[l].isalnum() or s[l]==' '):
                l+=1
            while r > -1 and (not s[r].isalnum() or s[r] == ' '):
                r-=1
            if r < 0 or l == len(s): break # OOB
            if s[l].lower() != s[r].lower():
                return False 
            l+=1
            r-=1

        return True
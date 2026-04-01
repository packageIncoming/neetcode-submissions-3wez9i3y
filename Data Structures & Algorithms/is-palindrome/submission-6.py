class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1
        while l <=r:
            while l < len(s) and s[l].isalnum() is False:
                l+=1
            while r > -1 and s[r].isalnum() is False:
                r-=1
            if l > r: break
            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l < r:
            while l < len(s) and s[l].isalnum() == False:
                l+=1
            while r > -1 and s[r].isalnum() == False:
                r-=1
            if l < len(s) and r > -1 and s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        return True
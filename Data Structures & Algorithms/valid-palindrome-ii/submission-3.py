class Solution:
    def validPalindrome(self, s: str) -> bool:

        l,r = 0, len(s)-1
        while l<=r:
            if s[l] != s[r]:
                # try by removing l
                sub = s[l+1:r+1]
                if sub == sub[::-1]:
                    return True
                # try by removing r
                sub = s[l:r]
                if sub == sub[::-1]:
                    return True
                return False

            l+=1
            r-=1
        return True
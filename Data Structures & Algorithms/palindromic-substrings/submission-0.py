class Solution:
    def countSubstrings(self, s: str) -> int:
        # isn't this the exact same as longest palindromic substring?
        palindromes = 0
        for mid in range(len(s)):
            l,r = mid,mid
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindromes+=1
                l-=1
                r+=1
            l,r = mid,mid+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindromes+=1
                l-=1
                r+=1

        return palindromes
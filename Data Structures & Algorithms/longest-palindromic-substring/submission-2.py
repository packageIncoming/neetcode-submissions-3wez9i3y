'''
11/24/25
Given a string s, return the longest substring of s that is a palindrome.
    -A palindrome is a string that reads the same forward and backward.
If there are multiple palindromic substrings that have the same length, return any one of them.
    -Multiple solutions possible but just need to return longest length one

Similar to  a previous problem which used some form of backtracking/recursion



'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(l,r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
    

        palindrome = [0,0]
        palindromeSize = 0
        for mid in range(len(s)):
            l = mid
            r = mid
            curPalindrome = [mid,mid]
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curPalindrome[0] = l
                curPalindrome[1] = r
                l-=1
                r+=1
            if curPalindrome[1]-curPalindrome[0]+1 > palindromeSize:
                palindrome=curPalindrome
                palindromeSize = curPalindrome[1]-curPalindrome[0]+1
            l = mid
            r = mid+1
            curPalindrome = [mid,mid]
            while l >= 0 and r < len(s) and s[l] == s[r]:
                curPalindrome[0] = l
                curPalindrome[1] = r
                l-=1
                r+=1
            if curPalindrome[1]-curPalindrome[0]+1 > palindromeSize:
                palindrome=curPalindrome
                palindromeSize = curPalindrome[1]-curPalindrome[0]+1
            


        return s[palindrome[0]:palindrome[1]+1]
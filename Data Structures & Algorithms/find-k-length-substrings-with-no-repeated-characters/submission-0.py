'''
sliding window problem

! k can be larger than the length of s

semi brute force approach:
make a freq dict
when you have a window of size k,
    if the max of the freq dict is 1 then increment res
    shrink from left

max check becomes O(26) -> O(1)
Checking over s of length n
-> O(n) for linear scan

O(26) space complexity->O(1) space complexity

'''


class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:

        freq={}
        l=0
        res=0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r],0)+1
            if max(freq.values())==1 and (r-l+1)==k:
                res+=1
            if (r-l+1)==k:
                # now shrink right
                freq[s[l]]-=1
                l+=1
        return res

        
'''
Goal: Return the length of longest substring with only one distinct character
Can perform at most k replacements

If I have a string of length N and the most common letter appears N-X times
then I have to perform X replacements

If the number of replacements, X, is ever greater than k (X>k) then I have to
shorten the string until X <=k. 

While shortening, will the most common letter change?
YES
So we need to keep track of the most common letter too


AAABABB
A-AA-AAA-AAAB-AAABA-AAABAB-AABAB-ABAB-BAB-BABB


'''


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        N=len(s)

        longest=0
        freqs={}
        l=0
        maxFreq = 0

        for r in range(len(s)):
            # add the current letter
            c = s[r]
            freqs[c] = freqs.get(c,0)+1
            maxFreq = max(maxFreq,freqs[c])
            # do we have too many replacements?
            while (r-l+1) -maxFreq > k:
                # shrink from the left until we don't have too many replacements
                freqs[s[l]] = freqs[s[l]]-1
                l+=1
                # (remember to update mostCommonLetter) ?
            # update new size
            longest = max(longest,(r-l+1))
            #print(s[l:r+1])


        return longest
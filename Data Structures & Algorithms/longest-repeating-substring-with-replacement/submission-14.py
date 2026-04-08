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
        freqs=[0]*26
        mostCommonLetter=None
        l=0

        for r in range(len(s)):
            # add the current letter
            c = s[r]
            cIdx = ord(c)-ord('A')
            freqs[cIdx] +=1
            if mostCommonLetter is None or freqs[cIdx] > freqs[ord(mostCommonLetter)-ord('A')]:
                mostCommonLetter = c
            # do we have too many replacements?
            X = (r-l+1) - freqs[ord(mostCommonLetter)-ord('A')]
            while X > k:
                # shrink from the left until we don't have too many replacements
                # (remember to update mostCommonLetter) 
                lIdx = ord(s[l]) - ord('A')
                freqs[lIdx] -=1
                mostCommonLetter = chr(freqs.index(max(freqs)) + ord('A'))
                l+=1
                X = (r-l+1) - freqs[ord(mostCommonLetter)-ord('A')]
                
            # update new size
            longest = max(longest,(r-l+1))
            #print(s[l:r+1])


        return longest
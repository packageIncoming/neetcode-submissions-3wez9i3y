class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = defaultdict(int)
        mostFrequentChar = None
        curLength = 0
        longestLength  =0
        l=0
        for r in range(len(s)):
            chars[s[r]] +=1
            curLength+=1
           
            if( mostFrequentChar and chars[s[r]] > chars[mostFrequentChar]) or (mostFrequentChar is None):
                mostFrequentChar = s[r]
            mostFreq =  chars[mostFrequentChar]
            #print(f'most frequent up to idx {r}: {mostFrequentChar}')
            while l< r and curLength -  mostFreq > k:
                #print('need to shrink')
                chars[s[l]] -=1
                l+=1
                curLength = (r-l)+1
                

            print(s[l:r+1], curLength)
            print(r+1 - l)
            longestLength = max(longestLength,curLength)

        
        return longestLength
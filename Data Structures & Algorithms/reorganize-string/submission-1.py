class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = [0]*26 # correspond to 26 characters of alphabet
        for c in s:
            freq[ord(c)-ord('a')]+=1
        
        res=""
        if max(freq) > (len(s)+1)//2: return "" # cannot fit properly into the string

        while len(res) < len(s):
            maxFreqIndex = freq.index(max(freq))
            char = chr(maxFreqIndex+ord('a'))
            # add this character
            res+=char 
            freq[maxFreqIndex]-=1
            if freq[maxFreqIndex] == 0: continue # don't need to do anything else
            # add the next most frequent character
            tmp = freq[maxFreqIndex]
            freq[maxFreqIndex]=float('-inf') # so it doesn't count again
            secondMaxFreqIndex = freq.index(max(freq))
            secondChar = chr(secondMaxFreqIndex + ord('a'))
            res+=secondChar
            freq[secondMaxFreqIndex]-=1
            freq[maxFreqIndex]=tmp
        return res



        
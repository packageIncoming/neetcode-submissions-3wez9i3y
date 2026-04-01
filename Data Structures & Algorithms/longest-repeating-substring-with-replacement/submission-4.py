from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest_length = 0
        l_ptr = 0
        freqs = defaultdict(int)
        for r_ptr in range(len(s)):
            freqs[s[r_ptr]]+=1
            while r_ptr-l_ptr+1 - max(freqs.values()) > k:
                freqs[s[l_ptr]]-=1
                l_ptr+=1
            longest_length = max(longest_length,r_ptr-l_ptr+1)
        
        
        return longest_length
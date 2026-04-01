
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastSeen = defaultdict(int)
        for i in range(len(s)):
            lastSeen[s[i]] = max(i,lastSeen[s[i]])
        
        substrings = []
        #print(lastSeen)
        l,r=0,0
        while l < len(s) and r < len(s):
            orig_start = l
            l_char = s[l]
            r=lastSeen[l_char]
            while l < r:
                r = max(r,lastSeen[s[l]])
                l+=1
            #print(s[orig_start:r+1])
            substrings.append(r-orig_start+1)
            l=r+1
        return substrings
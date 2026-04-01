class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):return False
        # turn s1 into hashmap
        s1_hash = defaultdict(int)
        for i in range(len(s1)):
            s1_hash[s1[i]] +=1
        
        # iterate with a fixed size window of len(s1) over s2, with a hashmap that updates at every grow/shrink
        s2_hash = defaultdict(int)
        needs = len(s1_hash)
        haves = set()
        l, r = 0,0
        #print("looking for")
        #print(s1_hash)
        while r < len(s2):
            s2_hash[s2[r]]+=1
            if s2[r] in s1_hash and s2_hash[s2[r]] == s1_hash[s2[r]]:
                haves.add(s2[r])
            if (r-l)+1 > len(s1):
                #print("need to shrink")
                s2_hash[s2[l]]-=1
                if s2[l] in haves and s2[l] in s1_hash and s2_hash[s2[l]] < s1_hash[s2[l]]:
                    haves.remove(s2[l])
                l+=1
            #print(f"{haves}/{needs}")
            if len(haves) == needs:
                return True
            r+=1
        print(s2_hash,s1_hash)
        # if you find a matching hashmap return true otherwise return false

        return False
        
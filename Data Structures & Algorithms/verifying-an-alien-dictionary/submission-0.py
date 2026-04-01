class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # idea: convert order into a hashmap of [char:position] 
        # then iterate over pairs of words to check if they are lexicographically sorted (s1 < s2)
        if len(words) <=1: return True
        hmap = {}
        for i in range(len(order)):
            hmap[order[i]]=  i
        
        for i in range(len(words)-1):
            s1 = words[i]
            s2 = words[i+1]
            if len(s1) > len(s2) and s1[:len(s2)] == s2:
                return False
            for j in range( len(s1)):
                s1_c = s1[j]
                s2_c = s2[j]
                if s1_c != s2_c:
                    if hmap[s1_c] > hmap[s2_c]:
                        print(s1,s2)
                        print(s1_c,s2_c)
                        return False # lexicographically invalid
                    else:
                        break
        return True
